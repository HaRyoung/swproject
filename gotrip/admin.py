from django.contrib import admin

# Register your models here.
from .models import City
from .models import Festa
# Register your models here.
admin.site.register(City)
admin.site.register(Festa)