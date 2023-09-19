from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/posts/', views.PostsByCategoryView.as_view(), name='posts-by-category'),
    path('authors/<int:author_id>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
]