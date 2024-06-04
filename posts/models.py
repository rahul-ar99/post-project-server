from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to="posts/images/")
    description = models.TextField()
    like = models.IntegerField(default=0,null=False, blank=False)
    created_by = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "posts_post"

    def __str__(self):
        return self.title
