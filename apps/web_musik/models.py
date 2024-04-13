from django.db import models
from django.db.models import DO_NOTHING
from apps.users.models import User


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Categories(AbstractBaseModel):
    name = models.CharField(max_length = 50)

    def __str__(self): return self.name


class Video(AbstractBaseModel):
    title = models.CharField(max_length = 128)
    descriptions = models.TextField(null = True, blank = True)
    authors = models.ForeignKey(User, models.CASCADE, 'videos')
    video = models.FileField(upload_to = f'{authors.name}/videos/', null = False, blank = False)
    categories = models.ForeignKey(Categories, models.CASCADE, 'videos')
    is_active = models.BooleanField(default = True)
    is_download = models.BooleanField(default = False)

    class Meta:
        db_table = "Videos"

    def __str__(self): return self.title


class Comment(AbstractBaseModel):
    content = models.TextField()
    authors = models.ForeignKey(User, models.CASCADE, 'comments')
    videos = models.ForeignKey(Video, models.CASCADE, 'comments')

    class Meta:
        db_table = "Comments"

    def __str__(self): return f"{self.authors}-write comment-{self.videos}"


class VideoLike(AbstractBaseModel):
    authors = models.ForeignKey(User, models.CASCADE, 'video_likes')
    videos = models.ForeignKey(Video, DO_NOTHING, 'video_likes')

    class Meta:
        db_table = "Video_Likes"

    def __str__(self): return f"{self.authors}-like video-{self.videos}"


class CommentLike(AbstractBaseModel):
    authors = models.ForeignKey(User, models.CASCADE, 'comment_likes')
    comments = models.ForeignKey(Comment, DO_NOTHING, 'comment_likes')

    class Meta:
        db_table = "Comment_likes"

    def __str__(self): return f"{self.authors}-like comment-{self.comments}"
