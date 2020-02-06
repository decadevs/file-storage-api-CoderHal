from django.test import TestCase
from rest_framework.test import APIClient
from ..models import Bucket

# Create your tests here.

class TestBucketModel(TestCase):
    """ This class defines the test suite for the bucket model"""

    bucket_name = "TSV Folder"
    bucket = Bucket(name=bucket_name)

    def test_model_can_create_a_bucket(self):
        ''' Test if bucket can create a list'''
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)
  