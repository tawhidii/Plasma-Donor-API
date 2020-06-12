from django.db import models

class A_PositiveDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name


class A_NegativeDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name


class B_PositiveDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name


class B_NegativeDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name


class AB_PositiveDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name


class AB_NegativeDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name
    
class O_PositiveDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name

class O_NegativeDonorList(models.Model):
    name = models.CharField(max_length=100,blank=False)
    blood_group = models.CharField(max_length=20,blank=False)
    last_date_of_blood_donation = models.DateField()
    address = models.CharField(max_length=500,blank=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)



    CHECK_AVAILABLE = (
        ('available','available'),
        ('unavailable','unavailable')
    )
    
    GENDER = (
        ('male','Male'),
        ('female','Female')
    )

    available = models.CharField(max_length=15,choices=CHECK_AVAILABLE)
    gender    = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return self.name