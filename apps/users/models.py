from django.db import models
from django.contrib.auth.models import AbstractUser


# from apps.web_musik.models import Video


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


# class Playlist(AbstractBaseModel):
#     name = models.CharField(null = False, blank = False)
#     # videos = models.ForeignKey(Video, models.CASCADE, 'playlists')
#     description = models.TextField()
#
#     def __str__(self): return self.name


class User(AbstractUser):
    avatar = models.ImageField(upload_to = "users/", null = True, default = "users/user/logo.png")
    bio = models.TextField(null = True, blank = True)

    # playlists = models.ForeignKey(Playlist, models.CASCADE, 'authors', null = True, blank = True)

    class Meta:
        db_table = "Authors"

    def __str__(self) -> str: return self.username
