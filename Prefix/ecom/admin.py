from django.contrib import admin
from .models import Product
from .models import user_data
from .models import contact_data
# Register your models here.
admin.site.register(Product)
admin.site.register(user_data)
admin.site.register( contact_data)
