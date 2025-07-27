# config/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'contact']  # اسم URL nameهایی که در urls.py داری

    def location(self, item):
        return reverse(item)
