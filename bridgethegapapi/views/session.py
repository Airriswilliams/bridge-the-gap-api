"""View module for handling requests about sessions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Session


class SessionView(ViewSet):
    """Bridge the gap sessions view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single session

        Returns:
            Response -- JSON serialized session
        """
        session = Session.objects.get(pk=pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)
    # After getting the session, it is passed to the serializer. Then serializer.data
    # is passed to the Response as the response body.
        

    def list(self, request):
        """Handle GET requests to get all sessions

        Returns:
            Response -- JSON serialized list of sessions
        """
        sessions = Session.objects.all()
        # filter sessions by tutor or by parent
        tutor = request.query_params.get('tutor', None)
        if tutor is not None:
            sessions = sessions.filter(tutor_id=tutor)
        parent = request.query_params.get('parent', None)
        if parent is not None:
            sessions = sessions.filter(parent_id=parent)
            
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)
    # all is the equivalent of sql query select * from bridgethegapapi_session
    
# Serializer class determines how the Python data should be serialized back 
# to the client
class SessionSerializer(serializers.ModelSerializer):
    """JSON serializer for sessions
    """
    class Meta:
        model = Session
        fields = ('id', 'tutor', 'parent','date','time', 'skill_level')
        depth = 1
        
    # The Meta class holds the configuration for the serializer. The serializer is using
    # the Tutor model and including the id, tutor, parent, date, time , 'skill_level'fields
    
    
