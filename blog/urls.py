from django.conf.urls import include, url, re_path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

import weblog.urls
from weblog.sitemaps import WeblogSitemap

sitemaps = {
    'weblog': WeblogSitemap,
}

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='weblog/'), name='home'),
    re_path(r'^weblog/', include(weblog.urls)),
    re_path(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
