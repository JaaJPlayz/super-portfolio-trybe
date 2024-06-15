from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Profile, Project, Certificate, CertifyingInstitution
from .serializers import (
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    ProfileSerializer,
    ProjectSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            # busque o id do perfil
            # crie uma variável para guardar esse perfil

            person = Profile.objects.get(id=kwargs["pk"])

            return render(
                request,
                "profile_detail.html",
                {
                    "name": person.name,
                    "github": person.github,
                    "linkedin": person.linkedin,
                    "bio": person.bio,
                },
            )

        return super().retrieve(request, *args, **kwargs)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
