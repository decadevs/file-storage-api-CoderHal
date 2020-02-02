
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .mock_data import bucket_data
from ..models import Bucket


class TestBucketView(APITestCase):
    ''' Tests for different endpoints'''
    def setUp(self):
        Bucket.objects.create(**bucket_data.bucket_data())
        self.url = reverse('bucket')+'?id=1' 

    def test_api_can_create_bucket(self):
        url = reverse("buckets")
        response= self.client.post(url,bucket_data.bucket_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'],bucket_data.bucket_data()['name'])



