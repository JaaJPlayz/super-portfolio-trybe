from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Project)
admin.site.register(models.Certificate)
admin.site.register(models.CertifyingInstitution)
