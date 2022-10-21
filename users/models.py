from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # the profile must have one-to-one relationship with the logged in user

    # CASCADE: delete profile if user is delete.
    # But leave user if profile is deleted.
    user = models.OneToOneField(User, on_deete=models.CASCADE)

