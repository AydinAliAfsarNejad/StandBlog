from django.db import models


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter

    @property
    def filter(self):
        return filter(lambda post: post.status == True, self.get_queryset())