import os
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.utils import timezone

# from django.contrib.auth.models import User
"""
- 장고에서 기본 제공하는 User Model 이 User를 직접 사용하는 것은 권장되지 않음.
- 만약 내가 custom으로 유저 모델을 만들었다면 settings.py에 꼭 명시해줘야함.
- settings.py에 현재 User Model로 명시되어 있는 것을 가져옴
- AUTH_USER_MODEL은 프로젝트 초기에 설정해주는 것이 가장 BEST
"""


def uuid_name_upload_to(instance, filename):
    # app_label = instance.__class__._meta.app_label  # 앱 별로
    app_label = instance._meta.app_label  # 앱 별로
    cls_name = instance.__class__.__name__.lower()  # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d')  # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고 소문자로 변환
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])


class InstagramPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    # photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'instagram_post'
        verbose_name = 'Instagram 게시글'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return f'({self.pk}) Instagram 게시글'

    """
    자주 쓰는 로직이라면 model에서 구현 아니라면 admin에서 구현
    """
    # def message_length(self):
    #     return f'{len(self.message)}'
    # message_length.short_description = '메세지 글자수'


class InstagramPostComment(models.Model):
    post = models.ForeignKey(
        InstagramPost,
        on_delete=models.CASCADE,
        # post model의 `is_public` field가 특정 값인 것만 지정할 수 있도록 하는 옵션
        limit_choices_to={'is_public': True}
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'instagram_post_comment'
        verbose_name = 'instagram 게시글 댓글'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'({self.pk}) Instagram 게시글 댓글'
