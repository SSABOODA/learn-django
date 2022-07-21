from django.db import models
from utils.media_lib import uuid_name_upload_to


class InstagramPost(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    # photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to())
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'instagram_post'
        verbose_name = 'Instagram 게시글'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'({self.pk}) Instagram 게시글'

    # 자주 쓰는 로직이라면 model에서 구현 아니라면 admin에서 구현
    # def message_length(self):
    #     return f'{len(self.message)}'
    # message_length.short_description = '메세지 글자수'
