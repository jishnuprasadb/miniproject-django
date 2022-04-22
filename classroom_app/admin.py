from django.contrib import admin

# Register your models here.
from classroom_app import models


admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Complaint)
admin.site.register(models.Notification)