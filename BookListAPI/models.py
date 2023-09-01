from django.db import models

# Create your Book model here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    inventory = models.IntegerField(default=100)
# Create Meta class inside the Book model
    def Meta(self):
        models.Index(fields=["price"])

