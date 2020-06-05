from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from department.models import Department, Course


#                                        create new user

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, i_am, password):
        if not email:
            raise ValueError('User must have an email address.')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, i_am=i_am)

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email, i_am, password):
        user = self.create_user(first_name, last_name, email, i_am, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    ACCOUNT_TYPE = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    i_am = models.CharField(max_length=7, choices=ACCOUNT_TYPE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'i_am']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def academic_info(self):
        if self.i_am == 'teacher':
            return self.teacherinfo
        elif self.i_am == 'student':
            return self.studentinfo
        elif self.i_am == 'staff':
            return self.staffinfo
    
    def __str__(self):
        return self.get_full_name()+f'({self.i_am})'


#                                           user information

class UserInfo(models.Model):
    SELECT_GENDER = (('Male', 'Male'), ('Female', 'Female'))
    user = models.OneToOneField(UserAccount , on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=SELECT_GENDER, null=True)
    birth_date = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.png')
    facebook_url = models.URLField(null=True, blank=True)
    _account_created = models.DateField(auto_now_add=True)
    _account_updated = models.DateField(auto_now=True)


    def __str__(self):
        return self.user.get_full_name()


#                                           user phone number

class Phonebook(models.Model):
    user = models.ForeignKey(UserAccount, related_name='phone', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()


#                                      student table

class StudentInfo(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, primary_key=True)
    student_id = models.BigIntegerField(unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    batch = models.SmallIntegerField(null=True)
    section = models.CharField(max_length=2, null=True)
    session = models.CharField(max_length=20, null=True, blank=True)
    registration = models.BigIntegerField(unique=True, null=True, blank=True)
    addmission_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


#                                       teacher table

class TeacherInfo(models.Model):
    MARITAL_STATUS = (('Married', 'Married'), ('Unmarried', 'Unmarried'))
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, primary_key=True)
    is_verified = models.BooleanField(default=False)
    teacher_id = models.BigIntegerField(unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    degree = models.TextField(null=True, blank=True)
    course_takes = models.ManyToManyField(Course, related_name='course_takes', default=None)
    marital_status = models.CharField(max_length=9, choices=MARITAL_STATUS, null=True)
    joining_date = models.DateField(null=True, blank=True)

    @property
    def course_info(self):
        return self.course_takes

    def __str__(self):
        return self.user.get_full_name()


class StaffInfo(models.Model):
    MARITAL_STATUS = (('Married', 'Married'), ('Unmarried', 'Unmarried'))
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    designation = models.CharField(max_length=255, null=True)
    qualifications = models.TextField(null=True, blank=True)
    marital_status = models.CharField(max_length=9, choices=MARITAL_STATUS, null=True)
    joining_date = models.DateField(null=True)

    def __str__(self):
        return self.user.get_full_name()