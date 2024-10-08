from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, permissions, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer
from .models import Post, Followers
from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend  # Added for filtering
from rest_framework.pagination import PageNumberPagination

# Custom Pagination for posts
class PostPagination(PageNumberPagination):
    page_size = 10  # Specify default page size
    page_size_query_param = 'page_size'
    max_page_size = 100  # Limit for page size

# Registration View
@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone can access registration
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# User Logout View
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# Post List and Create View
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination  # Add pagination class for paginated results
    filter_backends = [DjangoFilterBackend]  # Add filter backend for filtering posts
    filterset_fields = ['content']  # Allow filtering by content field

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Post Detail, Update, and Delete View
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter posts to only allow users to manage their own posts
        return self.queryset.filter(user=self.request.user)

# Follow User View
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Require the user to be authenticated
def follow_user(request, username):
    try:
        # Find the user that is to be followed
        user_to_follow = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Prevent users from following themselves
    if request.user == user_to_follow:
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the user is already following the target user
    follow, created = Followers.objects.get_or_create(user=request.user, following=user_to_follow)

    if created:
        return Response({'message': f'You are now following {username}'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': f'You are already following {username}'}, status=status.HTTP_400_BAD_REQUEST)

# Unfollow User View
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Require the user to be authenticated
def unfollow_user(request, username):
    try:
        # Fetch the user that is to be unfollowed
        user_to_unfollow = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the current user is following the user_to_unfollow
    try:
        follow = Followers.objects.get(user=request.user, following=user_to_unfollow)
        follow.delete()  # Remove the follow relationship
    except Followers.DoesNotExist:
        return Response({'error': 'You are not following this user'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create the user with hashed password
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])  # Hash the password
        )
        user.save()
        return user
