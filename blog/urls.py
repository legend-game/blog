from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

from weblog.sitemaps import WeblogSitemap
sitemaps = {
    'weblog': WeblogSitemap,
}

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='weblog/'), name='home'),
    url(r'^weblog/', include('weblog.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
            {'sitemaps':sitemaps}),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
