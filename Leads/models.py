from django.db import models
from django.contrib.auth.models import get_user_model

Uaer=get_user_model()

# Create your models here.

class Lead(models.Model):


    # SOURECE_CHOICES = (('youtube', 'youtube'),
    
    # ('twiter', 'twiter'),
    # ('googleplus', 'googleplus'),
    # )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    # Phoned=models.BooleanField(default=False)
    # sources = models.char_field(choices=SOUREC_SOURCE,max_length=100)
    # profiles = models.ImageField(null=True, blank=True)
    # Special_files = models.FileField(null=True, blank=True)

class Agent(models.Model):
    user=models.ForeignKey(Uaer,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
