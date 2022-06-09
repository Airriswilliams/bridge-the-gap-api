"""View module for handling requests about parents"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Parent


class ParentView(ViewSet):
    """Bridge the gap parents view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single parent

        Returns:
            Response -- JSON serialized parent
        """
        try:
            parent = Parent.objects.get(pk=pk)
            serializer = ParentSerializer(parent)
            return Response(serializer.data)
        except Parent.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    # After getting the parent, it is passed to the serializer. Then serializer.data
    # is passed to the Response as the response body.
        

    def list(self, request):
        """Handle GET requests to get all parents

        Returns:
            Response -- JSON serialized list of parents
        """
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)
    # all is the equivalent of sql query select * from bridgethegapapi_parent
    
# Serializer class determines how the Python data should be serialized back 
# to the client
class ParentSerializer(serializers.ModelSerializer):
    """JSON serializer for parents
    """
    class Meta:
        model = Parent
        fields = ('id', 'user', 'child_name','child_age')
        
    # The Meta class holds the configuration for the serializer. The serializer is using
    # the Parent model and including the id, user, child_name, child_age fields
    
    
