from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, primary_key=True)
    head_of_department = models.CharField(max_length=100, null=True)    # teacher_id
    start_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.code


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=50, primary_key=True)
    credit = models.FloatField(null=True)
    topics = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Holiday(models.Model):
    reason = models.CharField(max_length=255, null=True)
    date = models.DateField( null=True)

    def __str__(self):
        return self.reason
        

class Calender(models.Model):
    event_type = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    event_id = models.IntegerField(null=True)   # routine or holiday id

    def __str__(self):
        return f'{self.event_type}-{self.date}'