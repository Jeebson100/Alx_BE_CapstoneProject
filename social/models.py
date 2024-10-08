from django.contrib.auth.models import User
from django.db import models

# UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Post Model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    media = models.ImageField(upload_to='post_media/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:30]}'

# Followers Model
class Followers(models.Model):
    user = models.ForeignKey(User, related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers_set', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'following')

    def __str__(self):
        return f'{self.user.username} follows {self.following.username}'
