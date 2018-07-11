from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^alltheaters$', views.alltheaters, name="alltheaters"),
    url(r'^cities$', views.cities, name="cities"),
    url(r'^movies$', views.movies, name="movies"),
    url(r'^send_request$', views.send_request, name="send_request"),
]