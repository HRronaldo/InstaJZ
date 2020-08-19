from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):   # 创建一个Post，这个Post是django.db里面的models里面的Model这个类的一个子类
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class InstaUser(AbstractUser): 
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )
        