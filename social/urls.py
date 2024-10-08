from django.urls import path
from .views import PostListCreateView, PostDetailView, follow_user, unfollow_user, register_user
from rest_framework.authtoken.views import obtain_auth_token  # Import DRF's token view

urlpatterns = [
    # Post URLs
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Follow and Unfollow URLs
    path('follow/<str:username>/', follow_user, name='follow-user'),
    path('unfollow/<str:username>/', unfollow_user, name='unfollow-user'),

    # User registration URL
    path('register/', register_user, name='register-user'),

    # Token authentication URL
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
