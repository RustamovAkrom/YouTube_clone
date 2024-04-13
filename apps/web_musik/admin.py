from django.contrib import admin
from apps.web_musik.models import Categories, Video, Comment, CommentLike, VideoLike


admin.site.register(Categories)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(VideoLike)
