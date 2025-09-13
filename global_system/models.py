from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()
    food_price = models.DecimalField(max_digits=10, decimal_places=2)

class Table(models.Model):
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    table_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_avaliable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.table_number}'

