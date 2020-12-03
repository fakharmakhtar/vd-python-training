from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    @property
    def display_price(self):
        return f'PKR {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
