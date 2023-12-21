from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from home.models import Article
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly, IsSuperUser
from .serializers import ArticleSerializer, UserSerializer, AuthorSerializer


class ArticleList(ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'my_slug'


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username']
    search_fields = ['title', 'description', 'author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ['status', 'publish']
    ordering = ['-publish']

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)
    #
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserList(ListCreateAPIView):
    permission_classes = [IsSuperUserOrStaffReadOnly]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrStaffReadOnly]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'my_username'


class UserViewSet(ModelViewSet):
    permission_classes = [IsSuperUserOrStaffReadOnly]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializer


class RevokeToken(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.auth.delete()
        return Response({'message': 'token revoked'}, status=status.HTTP_204_NO_CONTENT)
