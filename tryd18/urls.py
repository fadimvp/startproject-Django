from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tryd18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','team.views.home', name='home'),
    url(r'^contect/$','team.views.contect', name='contect'),
    url(r'^about/$','tryd18.views.about', name='about'),
    url(r'^out/$','team.views.loginout', name='out'),
    url(r'^shar/$', 'team.views.shar', name='shar'),
    url(r'^hour/$', 'team.views.hour', name='hour'),
    #url(r'^accounts/$', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
