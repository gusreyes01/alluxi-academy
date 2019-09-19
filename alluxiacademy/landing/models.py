from django.db import models
from django.core.validators import FileExtensionValidator

class Status(models.Model):    
    name = models.CharField(max_length=100)   
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    last_second_name = models.CharField(max_length=100, default="", blank=True)
    age = models.IntegerField()
    title = models.CharField(max_length=200)
    current_job = models.CharField(max_length=200)
    work_history = models.CharField(max_length=1000, default="")
    linkedin_account_link = models.CharField(max_length=150, blank=True)
    github_account_link = models.CharField(max_length=150, default="", blank=True)
    photo = models.ImageField(upload_to="", blank=True,validators=[FileExtensionValidator(['jpg','png'])])
    careers = models.ManyToManyField(Career, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.last_name

class Course(models.Model):
    title = models.CharField(max_length=200)
    advertising_phrase = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=750)
    summary = models.CharField(max_length=750, default="")
    duration_in_weeks = models.IntegerField()
    location = models.CharField(max_length=200)
    start_date = models.DateField(null=True,blank=True)
    start_hour = models.DateTimeField()
    finish_hour = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

class Phase(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title  + "-" + self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)    
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)

    def __str__(self):
        return self.phase.course.title + " - " + self.phase.name + " - "+ self.name
