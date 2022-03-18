from django.contrib import admin
from .models import User, Route
from .models import Car

# Register your models here.

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Route)