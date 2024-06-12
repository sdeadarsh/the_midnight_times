from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SearchKeyword, SearchResult
from django.contrib.auth.decorators import login_required
import requests
from datetime import datetime
from rest_framework import viewsets, permissions, status, views
from .searializers import SearchKeywordSerializer, SearchResultSerializer
from rest_framework.parsers import MultiPartParser, JSONParser
from django.core import paginator
from the_midnight_times.utils import errored_response, successfull_response
from users.models import User
from django.shortcuts import get_object_or_404
from newsapi import NewsApiClient

API_KEY = '808961e26f894a2ab663361c37dc84bb'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?'


class SearchKeywordViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SearchKeywordSerializer
    queryset = SearchKeyword.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        if not user_id:
            return successfull_response({}, "please pass the valid user_name")
        user = get_object_or_404(User, id=user_id)
        data = SearchKeyword.objects.filter(user=user)
        serialized = SearchKeywordSerializer(data, many=True)
        return successfull_response(serialized.data)
    
    def create(self, request, *args, **kwargs):
        try:
            page=request.GET.get('page',None)
            limit = request.GET.get('limit',None)
            keyword = request.data.get('searchBar', None)
            user_id = request.data.get('user_id', None)
            category = request.GET.get('category', None)
            language = request.GET.get('language', None)
            if not keyword or  not user_id:
                return successfull_response({},'Please enter something to search')
            user = get_object_or_404(User, id=user_id)
            existing_keyword = SearchKeyword.objects.filter(user=user, keyword=keyword).first()
            if existing_keyword:
                data_results = SearchResult.objects.filter(keyword=existing_keyword).values(
                    'title', 'description', 'url', 'published_at', 'img').order_by('published_at')
                if page and limit and int(limit)<len(list(data_results)):
                    data_results = self.add_pagination(list(data_results),page,limit)
                return successfull_response({'query': keyword, 'results': data_results})

            # Fetch results from News API

            newsapi = NewsApiClient(api_key='808961e26f894a2ab663361c37dc84bb')
            param = {'q':keyword}
            if category:
                param['category'] = category
            if language:
                param['language'] = language
            response = newsapi.get_top_headlines(**param)

            # response = requests.get(NEWS_API_URL, params={'q': keyword, 'apiKey': API_KEY})
            print(response)
            if response['totalResults'] ==0:
                return successfull_response({}, "No Data Found")
            
            data_results = []
            search_keyword = SearchKeyword.objects.create(user=user, keyword=keyword)
            for article in response['articles']:
                result = {
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'img': article['urlToImage'],
                    'published_at': datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%S%z')}
                data_results.append(result)
                SearchResult.objects.create(
                    keyword=search_keyword,
                    title=article.get('title', None),
                    description=article.get('description', None),
                    url=article.get('url', None),
                    img=article.get('urlToImage', None),
                    published_at=datetime.strptime(article.get('publishedAt', None), '%Y-%m-%dT%H:%M:%SZ')
                    )
                

            if page and limit and int(limit)<int(response['totalResults']):
                data_results = self.add_pagination(data_results,page,limit)
            
            return successfull_response({'query': keyword, 'results': data_results})

        except Exception as e:
            print('error', str(e))
            return errored_response("error in fetching the news")
        
    def add_pagination(self, dict_data, page, count):
        if page and count:
            p = paginator.Paginator(dict_data, count)
            return p.page(page).object_list

        return dict_data
            




@login_required
def results(request):
    keywords = SearchKeyword.objects.filter(user=request.user)
    context = {'keywords': keywords, 'error': False}
    return render(request, 'news_search_api/results.html', context)

class SearchResultViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SearchResultSerializer
    queryset = SearchResult.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']


    @login_required
    def results(request):
        keywords = SearchKeyword.objects.filter(user=request.user)
        context = {'keywords': keywords, 'error': False}
        return render(request, 'news_search_api/results.html', context)


    


