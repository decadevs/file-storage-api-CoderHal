from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 

from .models import Bucket
from ..bucket_serializer import BucketSerializer
# from ..bucket_serializer import BucketSerializer


class BucketList(APIView):
    
    def post(self, request, format=None):
        ''' creates a bucket instance'''

        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        ''' lists all buckets '''
        buckets = Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)