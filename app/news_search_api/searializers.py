from rest_framework import serializers
from .models import SearchKeyword, SearchResult


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeyword
        fields = "__all__"

class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = "__all__"
