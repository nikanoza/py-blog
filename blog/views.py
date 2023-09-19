from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Category, Author
from .serializers import PostSerializer, CategorySerializer, AuthorSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostsByCategoryView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Post.objects.filter(category_id=category_id)

class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer