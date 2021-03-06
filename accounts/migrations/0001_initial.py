# Generated by Django 3.0.6 on 2020-05-31 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('i_am', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('staff', 'Staff')], max_length=7)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_verified', models.BooleanField(default=False)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('present_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phonebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('teacher_id', models.BigIntegerField(null=True, unique=True)),
                ('designation', models.CharField(blank=True, max_length=20, null=True)),
                ('degree', models.TextField(blank=True, null=True)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=9, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('course_takes', models.ManyToManyField(default=None, to='department.Course')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='department.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.BigIntegerField(null=True, unique=True)),
                ('batch', models.SmallIntegerField(null=True)),
                ('section', models.CharField(max_length=2, null=True)),
                ('session', models.CharField(blank=True, max_length=20, null=True)),
                ('registration', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('addmission_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='department.Department')),
            ],
        ),
    ]
