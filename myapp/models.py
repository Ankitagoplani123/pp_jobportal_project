from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    
class ProfileForm(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    MS = (
        ('Married', 'Married'),
        ('Single', 'Single')
    )
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=SEX)
    experience_details = models.OneToOneField("ExperienceDetails", on_delete=models.CASCADE, null=True, blank=True)
    highest_degree = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10, choices=MS)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
       
class ExperienceDetails(models.Model):
    first_company = models.CharField(max_length=20)
    current_company = models.CharField(max_length=20)
    experience = models.IntegerField()
    job_post = models.CharField(max_length=30)

class CompanyDetails(models.Model):
    company_name = models.CharField(max_length=20)
    job_post = models.CharField(max_length=20)
    job_location = models.CharField(max_length=20)
    job_description = models.CharField(max_length=20)
    company_url = models.CharField(max_length=20)
    job_skill_set = models.ManyToManyField("JobSkillSet", null=True, blank=True)
    
class JobSkillSet(models.Model):
    skill_name = models.CharField(max_length=20)
    
    
    
    

