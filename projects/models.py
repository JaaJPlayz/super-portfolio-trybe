from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    github = models.URLField(null=False, blank=False, max_length=500)
    linkedin = models.URLField(null=False, blank=False, max_length=500)
    bio = models.TextField(null=False, blank=False, max_length=500)

    #
    # def get_profiles(self):
    #     return Profile.objects.all()
    #
    # def get_profile_by_id(self, id):
    #     return Profile.objects.get(id=id)
    #
    # def create_profile(self, name, github, linkedin, bio):
    #     return Profile.objects.create(
    #         name=name, github=github, linkedin=linkedin, bio=bio
    #     )
    #
    # def update_profile(self, id, name, github, linkedin, bio):
    #     profile = Profile.objects.get(id=id)
    #     profile.name = name
    #     profile.github = github
    #     profile.linkedin = linkedin
    #     profile.bio = bio
    #     profile.save()
    #
    # def delete_profile(self, id):
    #     profile = Profile.objects.get(id=id)
    #     profile.delete()
    #
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False, max_length=500)
    github_url = models.URLField(null=False, blank=False, max_length=500)
    keyword = models.CharField(max_length=50, null=False, blank=False)
    key_skill = models.CharField(max_length=50, null=False, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # def get_projects(self):
    #     return Project.objects.all()
    #
    # def get_project_by_id(self, id):
    #     return Project.objects.get(id=id)
    #
    # def create_project(
    #     self, name, description, github_url, keyword, key_skill, profile
    # ):
    #     return Project.objects.create(
    #         name=name,
    #         description=description,
    #         github_url=github_url,
    #         keyword=keyword,
    #         key_skill=key_skill,
    #         profile=profile,
    #     )
    #
    # def update_project(
    #     self, id, name, description, github_url, keyword, key_skill, profile
    # ):
    #     project = Project.objects.get(id=id)
    #     project.name = name
    #     project.description = description
    #     project.github_url = github_url
    #     project.keyword = keyword
    #     project.key_skill = key_skill
    #     project.profile = profile
    #     project.save()
    #
    # def delete_project(self, id):
    #     project = Project.objects.get(id=id)
    #     project.delete()
    #
    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(null=False, blank=False, max_length=500)

    # def get_certifying_institutions(self):
    #     return CertifyingInstitution.objects.all()
    #
    # def get_certifying_institution_by_id(self, id):
    #     return CertifyingInstitution.objects.get(id=id)
    #
    # def create_certifying_institution(self, name, url):
    #     return CertifyingInstitution.objects.create(name=name, url=url)
    #
    # def update_certifying_institution(self, id, name, url):
    #     certifying_institution = CertifyingInstitution.objects.get(id=id)
    #     certifying_institution.name = name
    #     certifying_institution.url = url
    #     certifying_institution.save()
    #
    # def delete_certifying_institution(self, id):
    #     certifying_institution = CertifyingInstitution.objects.get(id=id)
    #     certifying_institution.delete()

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
        # null=False,
        max_length=500,
    )
    #
    # def get_certificates(self):
    #     return Certificate.objects.all()
    #
    # def get_certificate_by_id(self, id):
    #     return Certificate.objects.get(id=id)
    #
    # def create_certificate(
    #     self, name, certifying_institution, timestamp, profiles
    # ):
    #     return Certificate.objects.create(
    #         name=name,
    #         certifying_institution=certifying_institution,
    #         timestamp=timestamp,
    #         profiles=profiles,
    #     )
    #
    # def update_certificate(
    #     self, id, name, certifying_institution, timestamp, profiles
    # ):
    #     certificate = Certificate.objects.get(id=id)
    #     certificate.name = name
    #     certificate.certifying_institution = certifying_institution
    #     certificate.timestamp = timestamp
    #     certificate.profiles = profiles
    #     certificate.save()
    #
    # def delete_certificate(self, id):
    #     certificate = Certificate.objects.get(id=id)
    #     certificate.delete()

    def __str__(self):
        return self.name
