from django.contrib import admin
import firstapp.models  # Import your models to register them
# Register your models here.
admin.site.register(firstapp.models.Product)  # Register the Product model