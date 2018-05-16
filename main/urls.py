from django.conf.urls import patterns, include, url

from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',views.index,name='index'),
    url(r'^hcubslive.fl/qH7dVijk9AE8cdWn/',views.hcubs,name='hcubs'),
    url(r'^create-new-user/',views.createnewuser,name='createnewuser'),
    url(r'^saveform/',views.saveform,name='saveform'),
    url(r'^hcubslive.fll/qH7dVijk9AE8cdWn/',views.diversion,name='hcubslive'),
    url(r'^checklogin/',views.checklogin,name='checklogin'),
    url(r'^createnewuserdetails/',views.createnewuserdetails,name='createnewuserdetails'),

     
   	  

    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^kimlee/', include('cart.urls')),


)

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)