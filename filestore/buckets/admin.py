from django.contrib import admin

# Register your models here.
from .models.bucket import Bucket

admin.site.register(Bucket)