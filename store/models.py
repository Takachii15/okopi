from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse


customer = get_user_model()


# Product models
class Item(models.Model):

    CATEGORIES = (
            ('AK', 'Alat Kopi'),
            ('BK', 'Biji Kopi'),
            ('KL', 'Kopi Liter'),
            ('TH', 'Teh')
            )

    title       = models.CharField(max_length=255)
    description = models.TextField() 
    price       = models.FloatField()
    category    = models.CharField(choices=CATEGORIES, verbose_name='kategori' ,max_length=5, blank=True)
    slug        = models.SlugField(max_length=255)
    image_main  = models.ImageField(upload_to='photos/products/%Y%m/%d/')
    image_1     = models.ImageField(upload_to='photos/products/%Y%m/%d/') 
    image_2     = models.ImageField(upload_to='photos/products/%Y%m/%d/', blank=True)
    image_3     = models.ImageField(upload_to='photos/products/%Y%m/%d/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:")


# Cart per Item
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=CASCADE) 

    def __str__(self):
        return self.item.title


# User's cart models
class Order(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items       = models.ManyToManyField(OrderItem)
    start_date  = models.DateField(auto_now_add=True)
    ordered     = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
