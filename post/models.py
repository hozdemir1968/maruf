from django.db import models

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-publish_date']


class Comment(models.Model):
    post=models.ForeignKey('post.Post',related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name