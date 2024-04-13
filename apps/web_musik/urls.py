from django.urls import path
from .views import HomePageView, PlayVideoPageView, ExplorePageView, SearchVideo

app_name = "musiks"

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('video-detail/<pk>', PlayVideoPageView.as_view(), name = 'video-detail'),
    path('video-explore/', ExplorePageView.as_view(), name='video-explore'),
    path('searching/', SearchVideo.as_view(), name='video-search')
]
