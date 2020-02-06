from django.contrib import admin

# Register your models here.
from buckets.models import Bucket

admin.site.register(Bucket)