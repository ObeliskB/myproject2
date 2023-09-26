from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name + " [" + str(self.price) + " baht]"