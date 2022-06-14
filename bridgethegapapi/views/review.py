"""View module for handling requests about reviews"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bridgethegapapi.models import Review, Tutor
from bridgethegapapi.models import Parent


class ReviewView(ViewSet):
    """Bridge the gap reviews view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single review

        Returns:
            Response -- JSON serialized review
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()
        
        # tutor = request.query_params.get('tutor', None)
        # if tutor is not None:
        #     reviews = reviews.filter(tutor_id=tutor)
        
       
    # "all" method gets every reviewer that reviewed that game. The conditional,"player in review"
        # the review variable is now a list of Review objects. adding many=true lets the serializer know
        # that a list vs. a single object is to be serialized.
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        
        parent = Parent.objects.get(user=request.auth.user)
        tutor = Tutor.objects.get(pk=request.data["tutor_id"])
        
        review = Review.objects.create(
           tutor_review=request.data["tutor_review"],
           parent=parent,
           tutor=tutor
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def update(self, request, pk):
    
        review = Review.objects.get(pk=pk)
        serializer = CreateReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    
class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'tutor_review', 'parent','tutor')
        depth = 2


class CreateReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'tutor_review', 'parent','tutor')
