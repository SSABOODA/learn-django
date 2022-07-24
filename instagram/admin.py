from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import InstagramPost, InstagramPostComment

"""
Admin Resister 방법
"""

# 1. admin.site.register(InstagramPost)
# 2. admin.site.register(InstagramPost, InstagramPostAdmin)
# 3. @admin.register(InstagramPost)


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'photo_tag',
        'message',
        'is_public',
        'message_length',
        'created_at',
        'updated_at',
    ]
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, InstagramPost):
        if InstagramPost.photo:
            return mark_safe(f'<img src="{InstagramPost.photo.url}" style="width: 50px;" />')
        return None

    def message_length(self, post):
        return f'{len(post.message)} 글자'
    message_length.short_description = '메세지 글자수'


@admin.register(InstagramPostComment)
class InstagramPostCommentAdmin(admin.ModelAdmin):
    pass
