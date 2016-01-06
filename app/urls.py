from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news_analytics.views.landing_page'),
    url(r'^get_news/', 'news_analytics.views.get_content'),
    url(r'^signuppage/', 'news_analytics.views.signuppage'),
    url(r'^usersignup/', 'news_analytics.signuplogin.usersignup'),
    url(r'^loginpage/', 'news_analytics.signuplogin.loginpage'),
    url(r'^validateuser/', 'news_analytics.signuplogin.validateuser'),
    url(r'^errorpage/', 'news_analytics.signuplogin.errorpage')
    

)
