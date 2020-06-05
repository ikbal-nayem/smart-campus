from django.db import models
from department.models import Department, Course
from accounts.models import TeacherInfo

class ClassTest(models.Model):
    code = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    batch = models.SmallIntegerField( null=True)
    semester = models.SmallIntegerField( null=True)
    section = models.CharField(max_length=2, null=True)
    subject = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    topics = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    will_take = models.ForeignKey(TeacherInfo, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.department}-{self.subject.name}'
    
    

class Midterm(models.Model):
    code = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    batch = models.SmallIntegerField( null=True)
    semester = models.SmallIntegerField( null=True)
    set_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.department}-{self.batch} Batch (code: {self.code})'



class Final(models.Model):
    code = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING,  null=True)
    batch = models.SmallIntegerField( null=True)
    semester = models.SmallIntegerField( null=True)
    set_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.department}-{self.batch} Batch (code: {self.code})'



class MidRoutine(models.Model):
    exam = models.ForeignKey(Midterm, on_delete=models.CASCADE,  null=True)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True)
    date = models.DateField( null=True)
    time = models.TimeField( null=True)

    def __str__(self):
        return f'{self.exam.department}-{self.exam.code}-{self.subject}'



class FinalRoutine(models.Model):
    exam = models.ForeignKey(Midterm, on_delete=models.CASCADE,  null=True)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True)
    date = models.DateField( null=True)
    time = models.TimeField( null=True)

    def __str__(self):
        return f'{self.exam.department}-{self.exam.code}-{self.subject}'