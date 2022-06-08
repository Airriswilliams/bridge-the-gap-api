"""View module for handling requests about tutors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Tutor


class TutorView(ViewSet):
    """Bridge the gap tutors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tutor

        Returns:
            Response -- JSON serialized tutor
        """
        try:
            tutor = Tutor.objects.get(pk=pk)
            serializer = TutorSerializer(tutor)
            return Response(serializer.data)
        except Tutor.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    # After getting the tutor, it is passed to the serializer. Then serializer.data
    # is passed to the Response as the response body.
        

    def list(self, request):
        """Handle GET requests to get all tutors

        Returns:
            Response -- JSON serialized list of tutors
        """
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data)
    # all is the equivalent of sql query select * from bridgethegapapi_tutor
    
# Serializer class determines how the Python data should be serialized back 
# to the client
class TutorSerializer(serializers.ModelSerializer):
    """JSON serializer for tutors
    """
    class Meta:
        model = Tutor
        fields = ('id', 'user', 'bio','schedule','image_url')
        
    # The Meta class holds the configuration for the serializer. The serializer is using
    # the Tutor model and including the id, user, bio, schedule, image_url fields
    
    
