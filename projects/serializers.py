from rest_framework import serializers

from .models import Certificate, CertifyingInstitution, Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "certifying_institution",
            "profiles",
            "timestamp",
        ]

    def create(self, validated_data):
        profiles = validated_data.pop("profiles")
        certificate = Certificate.objects.create(**validated_data)
        certificate.profiles.set(profiles)
        return certificate


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates", [])
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate_data in certificates_data:
            certificate = Certificate.objects.create(**certificate_data)
            certifying_institution.certificates.add(certificate)
        return certifying_institution
