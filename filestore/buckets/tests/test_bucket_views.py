
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .mock_data import bucket_data
from ..models.bucket import Bucket


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


    def test_api_can_get_a_bucket(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete(self):
        
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_update(self):
       
        new_bucket = {'name': 'Updated'}
        response = self.client.put(self.url, new_bucket, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

