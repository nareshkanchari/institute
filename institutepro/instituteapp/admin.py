from django.contrib import admin
from .models import CoursesData


# Register your models here.

class AdminCoursesData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_dur',
                    'course_fee',
                    'start_date',
                    'start_time',
                    'trainer_name',
                    'trainer_exp'
                    ]


admin.site.register(CoursesData, AdminCoursesData)
