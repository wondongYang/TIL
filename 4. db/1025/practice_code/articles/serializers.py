from rest_framework import serializers
from articles.models import Article, Comment

# 여러개는 List로 만듬
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)
        # fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
        # depth = 1   # 1단계 더 자세한 정보를 가져올 때 사용


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 댓글 개수 출력
    # comment_first = serializers.CharField(source='comment_set.first', read_only=True)
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)

    # 만약 댓글 중 id 값이 15이하인 댓글을 찾고 싶다면..?
    comment_filter = serializers.SerializerMethodField('less_15')

    def less_15(self, article):
        qs = Comment.objects.filter(pk__lte=15, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data


    class Meta:
        model = Article
        fields = '__all__' 