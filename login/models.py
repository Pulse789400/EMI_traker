from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FSCODE = models.CharField(max_length=20,null=True, blank=True)
    Division = models.CharField(max_length=10, blank=True)
    Region = models.CharField(max_length=10, blank=True)
    Head_Quarter= models.CharField(max_length=10, blank=True)
    Design= models.CharField(max_length=10, blank=True)
    EMP_Code= models.CharField(max_length=10, blank=True)
    Reporting_Manager_Name= models.CharField(max_length=100, blank=True)
    Reporting_Manager_Code= models.CharField(max_length=10, blank=True)



class BaseSales(models.Model):
    Division = models.CharField(max_length=10, blank=True)
    Region = models.CharField(max_length=10, blank=True)
    Head_Quarter= models.CharField(max_length=10, blank=True)
    Category = models.CharField(max_length=10, blank=True)
    Group = models.CharField(max_length=10, blank=True)
    Final_Base_PCPM = models.DecimalField(
            max_digits=17,  # 10 digits before the decimal point + 5 digits after the decimal point
            decimal_places=0,  # 5 digits after the decimal point
                    )
    Date=models.DateField(
            # YYYY-MM-DD format
        )