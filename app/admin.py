from django.contrib import admin

from app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Feedback)
admin.site.register(models.creditcard)
admin.site.register(models.Payment)