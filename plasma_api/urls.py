# Main Project root url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from django.conf import settings
from plasma_api.views import index

urlpatterns = [
    path('apis/',include('plasma_donor_lists.urls')),
    path('become-donor/',include('become_donors.urls')),
    path('plasma-admin/', admin.site.urls),
    path('',index,name='index')
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
