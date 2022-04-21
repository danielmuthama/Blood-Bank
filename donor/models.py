from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BloodRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=255)
    tel = models.CharField(max_length=50, default=0)
    age = models.IntegerField(default=0)


class BloodDrive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=255)
    amount_wanted = models.IntegerField(default=0)


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save_donor(self):
        self.save()

    def delete_donor(self):
        self.delete()


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save_hospital(self):
        self.save()

    def delete_hospital(self):
        self.delete()
