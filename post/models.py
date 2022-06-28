from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

class Post(models.Model):
    title = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    title_bg = models.ImageField(upload_to='custom/',null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    editor = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    user_insta = models.CharField(max_length=200, default='simply._.shailesh')
    user_facebook = models.CharField(max_length=200, null=True, blank=True)
    user_twitter = models.CharField(max_length=200, null=True, blank=True)

    overview = models.TextField()

    sub_head_1 = models.CharField(max_length=200, null=True, blank=True)
    sub_head_1_top = models.TextField(null=True, blank=True)
    sub_head_1_img =models.ImageField(upload_to='custom/', null=True, blank=True) 
    sub_head_1_bottom = models.TextField(null=True, blank=True)

    sub_head_2 = models.CharField(max_length=200, null=True, blank=True)
    sub_head_2_top = models.TextField(null=True, blank=True)
    sub_head_2_img =models.ImageField(upload_to='custom/', null=True, blank=True) 
    sub_head_2_bottom = models.TextField(null=True, blank=True)

    sub_head_3 = models.CharField(max_length=200, null=True, blank=True)
    sub_head_3_top = models.TextField(null=True, blank=True)
    sub_head_3_img =models.ImageField(upload_to='custom/', null=True, blank=True) 
    sub_head_3_bottom = models.TextField(null=True, blank=True)

    sub_head_4 = models.CharField(max_length=200, null=True, blank=True)
    sub_head_4_top = models.TextField(null=True, blank=True)
    sub_head_4_img =models.ImageField(upload_to='custom/', null=True, blank=True) 
    sub_head_4_bottom = models.TextField(null=True, blank=True)

    sub_head_5 = models.CharField(max_length=200, null=True, blank=True)
    sub_head_5_top = models.TextField(null=True, blank=True)
    sub_head_5_img =models.ImageField(upload_to='custom/', null=True, blank=True) 
    sub_head_5_bottom = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title