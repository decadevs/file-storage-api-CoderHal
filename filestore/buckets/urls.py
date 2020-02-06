from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BucketDetail
from .views import BucketList
from buckets.models import Bucket

urlpatterns = [
    path('buckets/', BucketList.as_view(), name='buckets'),
    path('bucket/', BucketDetail.as_view(), name='bucket')

]

urlpatterns = format_suffix_patterns(urlpatterns)
