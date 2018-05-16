from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns =[
    # Examples:
    # url(r'^$', 'kimlee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^HCUBS/', include('main.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)