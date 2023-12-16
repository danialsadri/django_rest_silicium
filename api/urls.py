from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(prefix='article', viewset=views.ArticleViewSet, basename='article')
router.register(prefix='user', viewset=views.UserViewSet, basename='user')
app_name = 'api'
urlpatterns = [
    path('router/', include(router.urls)),
    path('article/list/', views.ArticleList.as_view(), name='article_list'),
    path('article/detail/<slug:my_slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('user/list/', views.UserList.as_view(), name='user_list'),
    path('user/detail/<str:my_username>/', views.UserDetail.as_view(), name='user_detail'),
    path('author/<int:pk>/', views.AuthorRetrieve.as_view(), name='author_detail'),
    path('revoke/', views.RevokeToken.as_view(), name='revoke_token'),
]
