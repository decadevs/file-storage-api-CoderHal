from django.contrib import admin

# Register your models here.
from .bucket import Bucket

admin.site.register(Bucket)