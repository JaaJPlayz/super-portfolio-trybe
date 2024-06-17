from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    github = models.URLField(null=False, blank=False, max_length=500)
    linkedin = models.URLField(null=False, blank=False, max_length=500)
    bio = models.TextField(null=False, blank=False, max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False, max_length=500)
    github_url = models.URLField(null=False, blank=False, max_length=500)
    keyword = models.CharField(max_length=50, null=False, blank=False)
    key_skill = models.CharField(max_length=50, null=False, blank=False)
    profile = models.ForeignKey(
        Profile, related_name="projects", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(null=False, blank=False, max_length=500)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        related_name="certificates",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        max_length=500,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, max_length=500
    )
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        blank=False,
        max_length=500,
    )

    def __str__(self):
        return self.name
