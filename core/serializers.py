from rest_framework import serializers
from .models import *
'''
ProfileSerializer
'''
class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Skill.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Profile
        fields = ['id','name','email','contact','about','curriculumVitae','skills','isSelected']
class ResumeSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Resume
        fields = ['id','applicant','file','datetime']
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields = ['id','name']
