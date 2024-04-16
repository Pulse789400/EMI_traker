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




"""

user_data =[{'username':'nbm1.hyderabad@pulsepharma.net','password':'8052','email':'nbm1.hyderabad@pulsepharma.net','FSCODE':'5LM156','Division':'NUCLEUS','Region':'TELANGANA','Head_Quarter':'HYDERABAD','Design':'BM','EMP_Code':'5605','Reporting_Manager_Name':'NALLURI SOLMON RAJU','Reporting_Manager_Code':'6404','first_name':'MIRZA AHMED ALI BAIG'}]

for data in user_data:
    user, created = User.objects.get_or_create(
        username=data['username'],
        defaults={
            'password': data['password'],
            'email': data['email'],
            'first_name': data['first_name']
        }
    )
    
    if created:
        profile = UserProfile(
            user=user,
            FSCODE=data['FSCODE'],
            Division=data['Division'],
            Region=data['Region'],
            Head_Quarter=data['Head_Quarter'],
            Design=data['Design'],
            EMP_Code=data['EMP_Code'],
            Reporting_Manager_Name=data['Reporting_Manager_Name'],
            Reporting_Manager_Code=data['Reporting_Manager_Code']
        )
        profile.save()
    else:
        print(f"User with username {data['username']} already exists.")

        """
