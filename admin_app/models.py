from django.db import models

# Create your models here.
class SkillChoice(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self) -> str:
        return f"{self.name}"
    
class Profile(models.Model):
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
    name=models.CharField(max_length=200)
    profession=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mob_no=models.CharField(max_length=40)
    avatar = models.ImageField(upload_to='profile_media')
    address=models.TextField(max_length=500)
    about=models.TextField(max_length=500)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    skills=models.ManyToManyField(to='admin_app.SkillChoice')
    dob= models.DateField()

    def __str__(self) :
        return f"{self.name}"

    
    


     
    