from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from cashkaro import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	    # Examples:
	    url(r'^$', 'cashkaro.views.home', name='home'),
	    #-------register,login & logout --------------------
	    url(r'^register/$','cashkaro.views.register'),
	    url(r'^login/$','cashkaro.views.login_view'),
	    url(r'^logout/$','cashkaro.views.logout_view'),
            #---------------------myorder &dashboard------------------------
	    url(r'^dashboard/$','cashkaro.views.dashboard'),
	    url(r'^myorder/$','cashkaro.views.myorders_view'),
            #------------------------------order-update url-----------------
	    url(r'^myorder/(?P<number>\d+)/$','cashkaro.views.order_update',name='order_update'),
	    
	    #-----------------------account change------------------------
	    	
	    url(r'^account/edit/$','cashkaro.views.account_edit'),

	   #----------------------redirect urls-------------------------------
	   url(r'^flipkart/$','cashkaro.views.flipkart_redirect'),




	    #--------------------------admin urls -----------------------
	    url(r'^admin/', include(admin.site.urls)),
	    #------------------------facebook-------------------------------
		(r'^facebook/', include('django_facebook.urls')),
		(r'^accounts/', include('django_facebook.auth_urls')),
	 
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
