from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    title = models.CharField(max_length=200)
    current_job = models.CharField(max_length=200)
    indeed_account = models.CharField(max_length=200)
    careers = models.ManyToManyField(Career)
    status = models.CharField(max_length=50)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    duration_in_weeks = models.IntegerField()
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    start_hour = models.DateTimeField()
    finish_hour = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class Phase(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    
