from django.db import models
from django.utils import timezone

from apps.user.models import UserProfile


class Base(models.Model):
    created = models.DateTimeField(db_column="dt_created", auto_now_add=True)
    updated = models.DateTimeField(db_column="dt_updated", default=timezone.now)

    class Meta:
        abstract = True


class Post(Base):
    title = models.CharField(
        db_column="ds_title", max_length=100, null=False, blank=False
    )
    subtitle = models.CharField(
        db_column="ds_subtitle", max_length=100, null=False, blank=False
    )
    type_post = models.PositiveIntegerField(db_column="in_type", null=False, blank=False)
    content = models.TextField(db_column="ds_content", null=False, blank=False)
    status = models.PositiveIntegerField(db_column="in_status", null=False, blank=False)
    keyword = models.ManyToManyField(db_column="ds_keyword", to="KeyWord", blank=False)
    user = models.ForeignKey(db_column="id_user", to=UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return str(self.title[:15])


class KeyWord(Base):
    name = models.CharField(db_column="ds_keyword", max_length=50, unique=True)

    class Meta:
        db_table = "tb_keywords"
        verbose_name = "KeyWords"
        verbose_name_plural = "KeyWords"

    def __str__(self):
        return str(self.name)
