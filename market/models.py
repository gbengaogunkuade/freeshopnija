from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify       # NEW


# Create your models here.

class MarketPostCategory(models.Model):
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1200)



    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "marketpostcategory"


    # Display the Title in the ADMIN page instead of the modelName
    def __str__(self):
        return self.category




class SellerMarketPost(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sellcategory = models.ForeignKey(MarketPostCategory, on_delete=models.PROTECT, related_name='sellcategorymenu')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=200, default='100')
    telephone_number = models.CharField(max_length=200, blank=False, default='08000000000')
    picture1 = models.URLField(default='default.jpg', null=True, blank=True)
    picture2 = models.URLField(default='default.jpg', null=True, blank=True)
    picture3 = models.URLField(default='default.jpg', null=True, blank=True)
    picture4 = models.URLField(default='default.jpg', null=True, blank=True)
    picture5 = models.URLField(default='default.jpg', null=True, blank=True)
    slug = models.SlugField(max_length=200, null=False, unique=False, default='')        # NEW




    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "SellerMarketPost"


    # Display the Title in the ADMIN page instead of the modelName
    def __str__(self):
        return self.seller.username




    # saving the model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # SLUGIFY
        super().save(*args, **kwargs)

        

    # absolute url
    def get_absolute_url(self):
        return reverse('market:detail', kwargs={'slug': self.slug})
