from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


# PROFILE MODEL
# INHERIT FROM THE DJANGO USER MODEL AND EDITING IT TO INCLUDE MORE FIELDS
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, blank=False, default='FREESHOP')
    delivery_address = models.TextField(blank=False, default='234, Johnson Street, Ikeja, Nigeria')
    telephone_number = models.CharField(max_length=200, blank=False, default='080')
    profile_picture_1 = models.ImageField(upload_to='profile_pictures', default='default.jpg')
    profile_picture_2 = models.ImageField(upload_to='profile_pictures', default='default.jpg')



    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "UserProfile"


    def __str__(self):
        return f'{self.user.username} Profile'



    # COMPRESS THE IMAGES UPLOADED TO THE MODEL ABOVE BEFORE SAVING INTO THE MODEL
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img1 = Image.open(self.profile_picture_1.path)
        img2 = Image.open(self.profile_picture_2.path)

        if (img1.height > 500 or img1.width > 500) or (img2.height > 500 or img2.width > 500):
            img1.thumbnail((500, 500))
            img2.thumbnail((500, 500))
            img1.save(self.profile_picture_1.path)
            img2.save(self.profile_picture_2.path)







