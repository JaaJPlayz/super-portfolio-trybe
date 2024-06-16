from rest_framework import serializers

from .models import Certificate, CertifyingInstitution, Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class SimplerCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name", "timestamp"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = SimplerCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, valid_data):
        cert_data = valid_data.pop("certificates")
        cert_institution = CertifyingInstitution.objects.create(**valid_data)
        for data in cert_data:
            Certificate.objects.create(
                certifying_institution=cert_institution,
                **data,
            )
        return cert_institution
