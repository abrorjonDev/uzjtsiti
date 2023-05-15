from django.urls import path

from customizer.views import HomeView, NewsView, NewsDetailView, TuzilmaView, IlmiyView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news', NewsView.as_view(), name='news'),
    path('news/<str:slug>', NewsDetailView.as_view(), name='news-detail'),
    path('t/<str:slug>', TuzilmaView.as_view(), name='tuzilma-detail'),
    path('i/<str:slug>', IlmiyView.as_view(), name='ilmiy-detail'),
]
