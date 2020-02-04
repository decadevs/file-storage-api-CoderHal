from rest_framework import serializers
from .bucket import Bucket
class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ['id', 'name', 'created_at']
    