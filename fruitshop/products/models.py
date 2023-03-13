from django.db import models

# Create your models here.
class Product(models.Model):

    nom  = models.CharField(max_length=200)
    prix = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

