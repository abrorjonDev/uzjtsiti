from django.urls import path

from customizer.views import HomeView, NewsView, NewsDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news', NewsView.as_view(), name='news'),
    path('news/<str:slug>', NewsDetailView.as_view(), name='news-detail'),
]
