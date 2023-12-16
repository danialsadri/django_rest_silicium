from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from home.models import Article


class ArticleList(ListView):
    template_name = 'home/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.filter(status=True)
        return articles


class ArticleDetail(DetailView):
    template_name = 'home/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        articles = get_object_or_404(Article, pk=self.kwargs.get('article_id'), status=True)
        return articles
