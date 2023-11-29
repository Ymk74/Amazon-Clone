from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile',null= True,blank=True)
    code = models.CharField(max_length=10,default=generate_code)


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(
            user = instance
        )




ADDRESS_TYPES = (
    ('Home','Home'),
    ('Business','Business'),
    ('Office','Office'),
    ('Academy','Academy'),
    ('Other','Other'),
)

class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ADDRESS_TYPES)
    address = models.TextField(max_length=300)
    notes = models.TextField(null=True,blank=True)



PHONE_TYPES = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
)

class Phone(models.Model):
    user = models.ForeignKey(User,related_name='user_phone', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=PHONE_TYPES)
    phone = models.CharField(max_length=25)