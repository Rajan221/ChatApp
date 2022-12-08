from django.db import models

# Create your models here.

class userDetails(models.Model):
    
    firstName = models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName
