from django.apps import AppConfig


class Blog1Config(AppConfig):
    # default_auto_field = 'django.db.models.AutoField'
    name = 'blog1'
    verbose_name = '블로그'
    verbose_name_plural = verbose_name
