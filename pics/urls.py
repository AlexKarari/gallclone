from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^singleimage/(\d+)', views.single_photo, name='singleImage'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
