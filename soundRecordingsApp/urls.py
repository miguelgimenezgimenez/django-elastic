from rest_framework import routers
# from django.conf.urls import url, include
from soundRecordingsApp import views, es_views
from django.urls import path

# router = routers.DefaultRouter()
# router.register(r'soundrecording', views.SoundRecordingViewSet)
# router.register(r'upload', views.upload_csv)

# urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^soundrecording-es$', es_views.ESSoundRecordingViewSet.as_view({'get': 'list'}))
    # url(r'^soundrecording-es$', es_views.ESSoundRecordingViewSet.as_view({'get': 'list'}))
    # url(r'^upload/', views.upload_csv)
# ]


app_name = 'soundRecordingsApp'

urlpatterns = [
    path('', views.upload_csv, name="list"),
    path('getmatches', views.getMatches, name="list"),
]
