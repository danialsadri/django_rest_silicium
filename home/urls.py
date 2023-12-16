from django.urls import path
from .import views


app_name = 'home'
urlpatterns = [
    path('article/list/', views.ArticleList.as_view(), name='article_list'),
    path('article/detail/<int:article_id>/', views.ArticleDetail.as_view(), name='article_detail'),
]
