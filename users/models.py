from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    is_complete = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    child_name = models.CharField(max_length=100, null=False, default="")
    child_age = models.IntegerField(null=False, default=0)

    father_name = models.CharField(max_length=100, null=False, default="")
    mother_name = models.CharField(max_length=100, null=False, default="")

    address = models.CharField(max_length=100, null=False, default="")
    current_college = models.CharField(max_length=100, null=False, default="")

    phone_number = models.CharField(max_length=100, null=False, default="")
    parent_phone_number = models.CharField(max_length=100, null=False, default="")

    bio = models.TextField()

    def __str__(self):
        return self.user.username
