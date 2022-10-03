from django.db import models
from django.utils import timezone

'''
A skill class for all the skills
many to many relation with Profile (Applicant)
'''
class Skill(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=15)
    curriculumVitae=models.FileField(upload_to='curriculumVitaes',null=True)
    isSelected=models.BooleanField(default=False)
    about=models.TextField(null=True)
    skills=models.ManyToManyField(Skill)
    def __str__(self) -> str:
        return self.name
'''
Below models created but not used in viewing
As I wasn'nt able to access these models in serializer class of Applicant
as backard relationship these relations are not many to many these are may to one 
(many projects one applicant) so 
'''
class Resume(models.Model):
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    file=models.FileField(upload_to='pdfs',null=True)
    datetime=models.DateTimeField(auto_now=True)
    #name=models.CharField(max_length=64)
    #datetime=models.DateTimeField(default=timezone.now)
'''
Below models created but not used in viewing
As wasn'nt able to access these models in serializer class
as backard relationship these relations are not many to many these are may to one 
(many projects one applicant) so 
I am using foreign key in Experiences,Education ...
'''
class Experience(models.Model):
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    position= models.CharField(max_length=64)
    institutionName = models.CharField(max_length=64)
    startDate=models.DateField()
    endDate=models.DateField(null=True)
    work=models.TextField()
    def __str__(self) -> str:
        return self.position + "|" + self.institutionName

class Project(models.Model):
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    startDate=models.DateField()
    endDate=models.DateField(null=True)
    work=models.TextField()
    

class Education(models.Model):
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    collegeName=models.CharField(max_length=64)
    startYear=models.DecimalField(max_digits=4,decimal_places=0)
    endYear=models.DecimalField(max_digits=4,decimal_places=0,null=True)
    def __str__(self) -> str:
        return self.collegeName

class Certification(models.Model):
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    certificationId=models.CharField(max_length=64,null=True)
    issuingAthority=models.CharField(max_length=64)
    issueDate = models.DateField()
    def __str__(self) -> str:
        return self.name

class Achievement(models.Model):
    #applicant=models.On
    applicant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    def __str__(self) -> str:
        return self.name