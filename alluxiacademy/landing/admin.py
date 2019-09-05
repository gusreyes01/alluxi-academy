from django.contrib import admin
from .models import Course
from .models import Instructor
from .models import Career
from .models import Phase

# Register your models here.
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Career)
admin.site.register(Phase)
