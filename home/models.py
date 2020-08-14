from django.db import models

# Create your models here.
class Announce(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-publish_date']
