from django.db import models


# Create your models here.

class FoodmapStore(models.Model):
    ratingcategories_choice = {
        ('四分或以上', '四分或以上'),
        ('三分', '三分'),
        ('兩分', '兩分'),
        ('兩分或以下', '兩分或以下'),
    }
    district = models.CharField(max_length=250)
    restaurantname = models.CharField(max_length=250)
    address = models.TextField()
    contactinfo = models.CharField(max_length=250)
    googlelink = models.TextField()
    openingtime = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    ratingintotaloffive = models.FloatField()
    ratingcategories = models.CharField(max_length=30, blank=True, null=True, choices=ratingcategories_choice)

    def __str__(self):
        return self.restaurantname
