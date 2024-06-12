import requests
from .models import SearchKeyword, SearchResult
from the_midnight_times.utils import successfull_response, errored_response
from django.shortcuts import get_object_or_404
from news_search_api.models import User
from newsapi import NewsApiClient
from datetime import datetime


API_KEY = '808961e26f894a2ab663361c37dc84bb'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def cron_for_updated_news(request):
        try:
            keyword = request.data.get('searchBar', None)
            user_id = request.data.get('user_id', None)
            if not keyword or  not user_id:
                return successfull_response({},'Please enter something to search')
            user = get_object_or_404(User, id=user_id)
            
            # Fetch results from News API
            # response = requests.get(NEWS_API_URL, params={'q': keyword, 'apiKey': API_KEY})
                        # /v2/everything
            newsapi = NewsApiClient(api_key=API_KEY)
            response = newsapi.get_everything(q=keyword,
                                                from_param='2017-12-01',
                                                to='2017-12-12',
                                                language='en',
                                                sort_by='latest')
            if response.status_code == 200:
                data = response.json()
                data_results = []
                search_keyword = SearchKeyword.objects.create(user=user, keyword=keyword)
                for article in data['articles']:
                    result = {
                        'title': article['title'],
                        'description': article['description'],
                        'url': article['url'],
                        'img': article['urlToImage'],
                        'published_at': datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')}
                    data_results.append(result)
                    SearchResult.objects.create(
                        keyword=search_keyword,
                        title=article.get('title', None),
                        description=article.get('description', None),
                        url=article.get('url', None),
                        img=article.get('urlToImage', None),
                        published_at=datetime.strptime(article.get('publishedAt', None), '%Y-%m-%dT%H:%M:%SZ')
                        )
                return successfull_response({'query': keyword, 'results': data_results})

        except Exception as e:
            print('error', str(e))
            return errored_response("error in fetching the news")