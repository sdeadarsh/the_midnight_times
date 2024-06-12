from django.core.management.base import BaseCommand
from django.urls import get_resolver, get_urlconf

class Command(BaseCommand):
    help = 'Displays all registered URL patterns'

    def handle(self, *args, **kwargs):
        urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        all_patterns = resolver.url_patterns
        
        def list_urls(lis, acc=None):
            if acc is None:
                acc = []
            for entry in lis:
                if hasattr(entry, 'url_patterns'):
                    list_urls(entry.url_patterns, acc)
                else:
                    acc.append(entry)
            return acc

        all_urls = list_urls(all_patterns)

        for url in all_urls:
            self.stdout.write(str(url.pattern))
