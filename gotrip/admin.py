from django.contrib import admin

# Register your models here.
from .models import City
from .models import Festa
from .models import Insta
# Register your models here.
admin.site.register(City)
admin.site.register(Festa)
admin.site.register(Insta)