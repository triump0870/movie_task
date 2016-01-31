from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from movie.models import Movie
from api.permissions import IsOwnerOrReadOnly
from api.serializers import MovieSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
# from rest_framework import mixins
# Create your views here.
User = get_user_model()

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
                    'users': reverse('api:user-list', request=request, format=format),
                    'movies': reverse('api:movie-list', request=request,format=format)
                    })
class MovieListView(generics.ListCreateAPIView):
    """
    List all the Movies, or create a new Movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,
                                    IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get(self, request):
    #     serializer =self.serializer_class(self.get_queryset(), many=True)
    #     return Response(serializer.data)

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Show the Movie dretails.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,
                                    IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    """
    List all the Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetial(generics.RetrieveAPIView):
    """
    Show the current user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
