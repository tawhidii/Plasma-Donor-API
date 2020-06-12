from django.db import models

class BecomePlasmaDonors(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    documents = models.FileField(upload_to='documents/%Y/%m/%d')


    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name

    
  
    




    