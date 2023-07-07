from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserList(generics.ListCreateApiView):
    queryset= get_user_model().objects.all()
    serializer_class=UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
# Create your views here.
