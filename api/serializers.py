from django.contrib.auth import get_user_model
from rest_framework import serializers
from home.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedIdentityField(view_name='api:author_detail')
    # author = serializers.CharField(source='author.username', read_only=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_author(self, obj):
        return obj.author.username + ' - ' + obj.author.email

    def validate_title(self, value):
        filter_list = ['php', 'laravel', 'javascript']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError(f"Don't use bad word! {value}")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
