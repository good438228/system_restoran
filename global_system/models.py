from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    table_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_avaliable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.table_number}'

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    custom_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Booking for {self.custom_name} in {self.table}'