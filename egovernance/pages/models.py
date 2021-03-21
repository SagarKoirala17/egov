from django.db import models

# Create your models here.
class Citizen(models.Model):

    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
    age=models.IntegerField(default=16)
    father_name=models.CharField(max_length=50,blank=True)
    husband_name = models.CharField(max_length=50,blank=True)
    mother_name=models.CharField(max_length=50,default=None)
    grandfather_name=models.CharField(max_length=50)
    father_citizen_number = models.CharField(max_length=12, blank=True)
    husband_citizenship_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    mother_citizen_number = models.CharField(max_length=12, blank=True,unique=True)
    husband_citizen_number = models.CharField(max_length=12, blank=True,unique=True)
    birth_certificate_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',default=None)
    father_citizenship_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    mother_citizenship_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    p_zone = models.CharField(max_length=50)
    p_district = models.CharField(max_length=50)
    p_village = models.CharField(max_length=50)
    p_ward = models.IntegerField()
    p_tole = models.CharField(max_length=50)
    p_house_no = models.IntegerField(blank=True)
    t_zone = models.CharField(max_length=50)
    t_district = models.CharField(max_length=50)
    t_village = models.CharField(max_length=50)
    t_ward = models.IntegerField()
    t_tole = models.CharField(max_length=50)
    t_house_no = models.IntegerField(blank=True)
    is_verified=models.BooleanField(default=False)


    def __str__(self):
        return self.first_name