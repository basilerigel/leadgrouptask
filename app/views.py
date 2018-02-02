from app.serializers import ProfileSerializer, PostSerializer, DrinkSerializer, UserSerializer
from app.models import Profile, Drink, Post
from rest_framework import generics, status
from django.contrib.auth.models import User
from app.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        drink = Drink.objects.get(pk=self.request.data['drink'])
        serializer.save(user=self.request.user, drink=drink)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except Drink.DoesNotExist:
            return Response({"details": "Drink object does not exists"},
                            status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DrinkList(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # renderer_classes = (renderers.json)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    ordering = ('id',)
    queryset = User.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
