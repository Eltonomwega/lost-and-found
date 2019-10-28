from django.db import models
from django.utils import timezone
from users.models import Stratizen
from PIL import Image


# Create your models here.

class Claim(models.Model):
    item_claimed = models.ForeignKey('Post',on_delete=models.CASCADE,null=True)
    claimed_by = models.ForeignKey(Stratizen, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_of_loss = models.DateField(default=timezone.now)
    date_claimed = models.DateTimeField(default=timezone.now)
    time_from = models.TimeField()
    time_to = models.TimeField()
    image = models.ImageField(default = 'default.png', upload_to='claims_images',null=True, blank=True, help_text='OPTIONAL! Upload any image of the item as proof of ownership!')
    accepted = models.BooleanField(null=True)

    def __str__(self):
        return str(self.claimed_by)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 650 or img.width < 650:
            output_size = (360, 360)
            img.thumbnail(output_size)
            img.save(self.image.path)
        if img.height > 650 or img.width > 650:
            output_size = (360, 360)
            img.thumbnail(output_size)
            img.save(self.image.path)

CATEGORY_CHOICES=(
    ('laptops', ("Laptops")),
    ('stationery', ("Stationery")),
    ('phones', ("Phones")),
    ('IDs', ("IDs")),
    ('Wallet & Purses', ("Wallet & Purses")),
    ('other', ("Other")),
)



class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100,default='other',choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    When = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='item_images')
    claimed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

#overiding the save method to resize images for faster loading of the website        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 650 or img.width < 650:
            output_size = (360, 360)
            img.thumbnail(output_size)
            img.save(self.image.path)
        if img.height > 650 or img.width > 650:
            output_size = (360, 360)
            img.thumbnail(output_size)
            img.save(self.image.path)


# Create your models here.



