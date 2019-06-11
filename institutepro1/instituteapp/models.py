from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.TextField(max_length=100)


class ContactData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

    COURSE_CHOICES = (
        ('py', 'yython'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )

    courses = MultiSelectField(max_length=200, choices=COURSE_CHOICES)

    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftn', 'Afternoon'),
        ('evng', 'Evening'),
        ('ngt', 'Night')
    )
    shifts = MultiSelectField(max_length=200, choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd','Hyderabad'),
        ('bang','Banglore'),
        ('chen', 'Chennai'),
        ('pune','Pune')
    )

    locations = MultiSelectField(max_length=200, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=50)
    start_date = models.DateField(max_length=100)


class CoursesData(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_dur = models.IntegerField()
    course_fee = models.IntegerField()
    start_date = models.DateField(max_length=100)
    start_time = models.TimeField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    trainer_exp = models.IntegerField()
