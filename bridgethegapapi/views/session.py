"""View module for handling requests about sessions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Session
from bridgethegapapi.models.parent import Parent
from bridgethegapapi.models.tutor import Tutor


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
    
    
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized session instance
        """
      
        tutor = Tutor.objects.get(user=request.auth.user)
        parent = Parent.objects.get(pk=request.data["parent"])
        

        session = Session.objects.create(
            date=request.data["date"],
            time=request.data["time"],
            skill_level=request.data["skill_level"],
            tutor=tutor,
            parent=parent
        )
        serializer = SessionSerializer(session)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a session

        Returns:
            Response -- Empty body with 204 status code
        """

        session = Session.objects.get(pk=pk)
        serializer = CreateSessionSerializer(session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
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
    
class CreateSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ('id', 'tutor', 'parent','date','time', 'skill_level')
        depth = 1  
