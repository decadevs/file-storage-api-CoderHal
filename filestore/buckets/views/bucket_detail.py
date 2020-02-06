from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 

from ..models import Bucket
from ..serializers import BucketSerializer


class BucketDetail(APIView):

    def get_bucket(self, pk):
        ''' gets the id of a bucket instance'''

        try:
            return Bucket.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404


    def get(self, request, format=None):
        ''' returns an instance of bucket'''
    
        bucket_id = request.GET.get("id")
        bucket = Bucket.objects.get(pk=int(bucket_id))
        serializer = BucketSerializer(bucket)
        return Response(serializer.data)


    def put(self, request, format=None):
        ''' updates an instance of a bucket'''

        bucket_id = request.GET.get("id")
        bucket = self.get_bucket(bucket_id)
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        ''' deletes an instance of bucket'''

        bucket_id = request.GET.get("id")
        bucket = self.get_bucket(bucket_id)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)