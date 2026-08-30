from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            {'name': 'website:index'},
            {'name': 'website:about'},
            {'name': 'website:contact'},
        ]

    def location(self, item):
        return reverse(item['name'])