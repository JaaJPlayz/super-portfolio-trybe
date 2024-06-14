from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    github = models.URLField(null=False, blank=False, max_length=500)
    linkedin = models.URLField(null=False, blank=False, max_length=500)
    bio = models.TextField(null=False, blank=False, max_length=500)

    def get_profiles(self):
        return Profile.objects.all()

    def get_profile_by_id(self, id):
        return Profile.objects.get(id=id)

    def create_profile(self, name, github, linkedin, bio):
        return Profile.objects.create(
            name=name, github=github, linkedin=linkedin, bio=bio
        )

    def update_profile(self, id, name, github, linkedin, bio):
        profile = Profile.objects.get(id=id)
        profile.name = name
        profile.github = github
        profile.linkedin = linkedin
        profile.bio = bio
        profile.save()

    def delete_profile(self, id):
        profile = Profile.objects.get(id=id)
        profile.delete()

    def __str__(self):
        return self.name
