from . import models
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'


class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = models.Assignment
        fields = '__all__'


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = models.Testimonial
        fields = '__all__'


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = models.BlogPost
        fields = '__all__'


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = models.Partner
        fields = '__all__'


class SocialLinkEmployee(ModelSerializer):
    class Meta:
        model = models.SocialLinkEmployee
        fields = '__all__'


class SocialLinkSerializer(ModelSerializer):
    class Meta:
        model = models.SocialLink
        fields = '__all__'


class RoleSerializer(ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'