from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib import messages
from django import forms
from customizer.models import News, Project, Partner, Message, Tuzilma, Ilmiy


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('is_archived',)


class HomeView(CreateView):
    template_name = "customizer/home.html"
    model = Message
    form_class = MessageForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        kwargs.update({
            "projects": Project.objects.all(),
            "partners": Partner.objects.all(),
            "news": News.objects.all()[:5],
            "tuzilma": Tuzilma.objects.all(),
            "ilmiy": Ilmiy.objects.all()
        })
        kwargs['projects2'] = kwargs['projects'][:5]
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Xabar qa'bul qilindi, tez orada siz bilan bog'lanamiz.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class NewsView(ListView):
    template_name = "customizer/news.html"
    queryset = News.objects.all()# .values('title', 'short_description', 'slug', 'image')
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        kwargs.update({
            "tuzilma": Tuzilma.objects.all(),
            "ilmiy": Ilmiy.objects.all(),
            "projects": Project.objects.all(),
            "news": News.objects.all()[:5],
        })
        return super().get_context_data(**kwargs)


class NewsDetailView(DetailView):
    template_name = "customizer/news_detail.html"
    queryset = News.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({
            "tuzilma": Tuzilma.objects.all(),
            "ilmiy": Ilmiy.objects.all(),
            "projects": Project.objects.all(),
            "news": News.objects.all()[:5],
        })
        return super().get_context_data(object_list, **kwargs)

class EmployeesView(ListView):
    template_name = "customizer/news.html"
    model = News
    context_object_name = 'team'


class ScientechView(ListView):
    template_name = "customizer/news.html"
    model = News
    context_object_name = 'team'


class TuzilmaView(DetailView):
    model = Tuzilma
    template_name = "customizer/tuzilma.html"
    lookup_field = 'slug'

    def get_context_data(self, **kwargs):
        kwargs.update({
            "page": "Tuzilma",
            "tuzilma": Tuzilma.objects.all(),
            "ilmiy": Ilmiy.objects.all(),
            "projects": Project.objects.all(),
            "news": News.objects.all()[:5],
        })
        return super().get_context_data(**kwargs)


class IlmiyView(DetailView):
    model = Ilmiy
    template_name = "customizer/tuzilma.html"
    lookup_field = 'slug'

    def get_context_data(self, **kwargs):
        kwargs.update({
            "page": "Ilmiy",
            "tuzilma": Tuzilma.objects.all(),
            "ilmiy": Ilmiy.objects.all(),
            "projects": Project.objects.all(),
            "news": News.objects.all()[:5],
        })
        return super().get_context_data(**kwargs)