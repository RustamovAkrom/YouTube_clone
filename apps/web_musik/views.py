from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from apps.web_musik.models import Video, Categories


class HomePageView(ListView):
    template_name = 'index.html'
    queryset = Video.objects.all()
    context_object_name = "videos"


class SearchVideo(View):
    def get(self, request):
        search = request.GET.get('search-video', None)
        if search:
            print(search)
            videos = Video.objects.filter(title__icontains = search)
            print(videos)
        else:
            videos = None
        return render(request, "index.html", {"videos": videos})


class PlayVideoPageView(View):
    def get(self, request, pk):
        video = Video.objects.get(pk = pk)
        videos = Video.objects.filter(categories = video.categories)
        return render(request, "web/play-video.html", {
            "video": video,
            "videos": videos
        })


class CanalAuthor(View):
    def get(self, request):
        author = request.user
        return render(request, "web/canal.html", {"author": author})


class ExplorePageView(ListView):
    template_name = 'web/explorer.html'
    queryset = Video.objects.all()
    context_object_name = 'videos'
