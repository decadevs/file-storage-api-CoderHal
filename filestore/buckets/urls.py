from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('buckets/', views.BucketList.as_view(), name='buckets'),
    path('bucket/', views.BucketDetail.as_view(), name='bucket')

]

urlpatterns = format_suffix_patterns(urlpatterns)
