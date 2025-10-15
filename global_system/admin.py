from django.contrib import admin
from .models import Food, Table,Booking,Review

admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Review)