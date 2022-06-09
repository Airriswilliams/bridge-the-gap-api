"""View module for handling requests about languages"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Language


class LanguageView(ViewSet):
    """Level up languages view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single language

        Returns:
            Response -- JSON serialized language
        """
        try:
            language = Language.objects.get(pk=pk)
            serializer = LanguageSerializer(language)
            return Response(serializer.data)
        except Language.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all languages

        Returns:
            Response -- JSON serialized list of languages
        """
        languages = Language.objects.all()
        # the language variable is now a list of Language objects. adding many=true lets the serializer know
        # that a list vs. a single object is to be serialized.
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
    
class LanguageSerializer(serializers.ModelSerializer):
    """JSON serializer for languages
    """
    class Meta:
        model = Language
        fields = ('id', 'language')
        # fields = (__all__)
# the Meta class holds the configuration for the serializer. We're telling the serializer to use the "Language" 
# model and to include the "id" and "language" fields
