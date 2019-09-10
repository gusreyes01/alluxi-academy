from django.contrib import admin
from .models import Course, Instructor, Career, Phase, Status, Topic

# Register your models here.
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Career)
admin.site.register(Status)
admin.site.register(Topic)

class TopicInline(admin.StackedInline):
    model = Topic
    extra = 0
    fields = ["name", "description"]

@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["name", "description", "course", "status"]
    inlines = [TopicInline]
