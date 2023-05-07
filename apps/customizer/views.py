from django.views.generic import TemplateView, ListView, DetailView

from customizer.models import News


class HomeView(TemplateView):
    template_name = "customizer/home.html"

    def get_context_data(self, **kwargs):
        kwargs.update({})
        return super().get_context_data(**kwargs)


class NewsView(ListView):
    template_name = "customizer/news.html"
    queryset = News.objects.all()# .values('title', 'short_description', 'slug', 'image')
    context_object_name = 'news'


class NewsDetailView(DetailView):
    template_name = "customizer/news_detail.html"
    queryset = News.objects.all()# .values('title', 'short_description', 'slug', 'image')
    # context_object_name = 'news'


class EmployeesView(ListView):
    template_name = "customizer/news.html"
    model = News
    context_object_name = 'team'


class ScientechView(ListView):
    template_name = "customizer/news.html"
    model = News
    context_object_name = 'team'
