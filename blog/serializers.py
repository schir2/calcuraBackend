from rest_framework import serializers

from blog.models import Article, Topic, Tag, ArticleSeries


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSeries
        fields = '__all__'
