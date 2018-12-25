from django.contrib import admin

from django.urls import include, path
from django.contrib import admin

api_urls = [
     path('', include('soundRecordingsApp.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
