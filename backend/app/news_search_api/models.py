from django.db import models
from users.models import User


class SearchKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    last_searched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword


class SearchResult(models.Model):
    keyword = models.ForeignKey(SearchKeyword, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    img = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
