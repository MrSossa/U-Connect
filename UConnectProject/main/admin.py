from django.contrib import admin
from .models import NavBar, User
from .models import Car
from .models import Logo
# Register your models here.

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Logo)
admin.site.register(NavBar)