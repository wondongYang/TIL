from django.shortcuts import get_list_or_404, get_object_or_404, render
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from articles import serializers

# Create your views here.

# article_list에서 @api_view를 사용하는 이유는
# 404
@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)    # Queryset
    serializer = ArticleListSerializer(articles, many=True)    # Json으로 만듬(Serialization)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)