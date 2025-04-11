from django.db import models
from django.contrib.auth.models import User

# Function for generating  a directory path for an uploaded image
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(blank=False)
    gender = models.CharField(choices=[("male", "male"), ("female", "female")], blank=False, max_length=6)
    gender.error_messages = {"invalid_choice":"You can only either be male or female."}
    userDescription = models.TextField(blank=True)
    profilePicture = models.ImageField(upload_to=user_directory_path, blank=True)

class Qualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workExperince = models.CharField(max_length=200)