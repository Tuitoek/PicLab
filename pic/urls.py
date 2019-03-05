from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url(r'^gallery/',views.gallery,name='gallery'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
