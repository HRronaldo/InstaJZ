from django.db import models
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