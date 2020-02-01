from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('buckets/', views.BucketList.as_view()),
    path('bucket/<int:pk>/', views.BucketDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
