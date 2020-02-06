from django.urls import path
from django.conf.urls import url
from .models.bucket import Bucket
from rest_framework.urlpatterns import format_suffix_patterns
from .views.bucket_detail import BucketDetail
from .views.bucket_list import BucketList

urlpatterns = [
    path('buckets/', BucketList.as_view(), name='buckets'),
    path('bucket/', BucketDetail.as_view(), name='bucket')

]

urlpatterns = format_suffix_patterns(urlpatterns)
