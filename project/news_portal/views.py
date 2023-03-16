from django.shortcuts import render
from datetime import datetime, timedelta
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 20


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'post.html'
    context_object_name = 'post'


