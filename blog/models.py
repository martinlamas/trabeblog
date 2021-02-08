from blog.utils import truncate
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, content: \
{truncate(self.content)}, likes: {self.likes}, creation_date: \
{self.creation_date}, last_update_date: {self.last_update_date}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id}, content: {truncate(self.content)}, likes: \
{self.likes}, creation_date: {self.creation_date}, last_update_date: \
{self.last_update_date}'
