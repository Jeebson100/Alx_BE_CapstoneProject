from django.contrib import admin
from .models import UserProfile, Post, Followers  # Correct model name is 'Followers'

# Register the models in the admin
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Followers)  # Correct model name
