from django.test import TestCase
from rest_framework.test import APIClient
from ..models import Bucket
from ..views import BucketDetail, BucketList
# from django.core.urlresolvers import reverse
# Create your tests here.

class ModelTestCase(TestCase):
    """ This class defines the test suite for the bucket model"""

    bucket_name = "TSV Folder"
    bucket = Bucket(name=bucket_name)

    def test_model_can_create_a_bucket(self):
        ''' Test if bucket can create a list'''
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)
  