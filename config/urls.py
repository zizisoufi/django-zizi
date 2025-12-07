from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from root.sitemaps import StaticViewSitemap

from root import views  # ایمپورت همه ویوها

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('root.urls')),          # مسیرهای اصلی اپ root
    path('services/', include('services.urls')),
    path('accounts/', include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),  # آدرس سایت‌مپ
    path('home/', views.home, name='home'),       # مسیر home
    path('about/', views.about, name='about'),    # مسیر about
    path('contact/', views.contact, name='contact'),  # مسیر contact
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
