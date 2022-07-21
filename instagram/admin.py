from django.contrib import admin
from .models import InstagramPost

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
        'message',
        'is_public',
        'message_length',
        'created_at',
        'updated_at',
    ]

    list_display_links = [
        'message',
    ]

    list_filter = [
        'created_at',
        'is_public',
    ]

    search_fields = [
        'message',
    ]

    def message_length(self, post):
        return f'{len(post.message)} 글자'
    message_length.short_description = '메세지 글자수'




