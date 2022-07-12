from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'({self.pk}) 게시글'
