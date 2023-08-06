from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly
from .serializers import UserPofileSerializers, PostProfileSerializers
from account.models import UserProfile
from publications.models import PostProfile
# Create your views here.


class UserProfileList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = UserPofileSerializers


class PostPorfileList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostProfile.objects.all()
    serializer_class = PostProfileSerializers


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = UserProfile.objects.all()
    serializer_class = UserPofileSerializers


class PostProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = PostProfile.objects.all()
    serializer_class = PostProfileSerializers
