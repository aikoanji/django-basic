from django.conf.urls import url
from src.province import views
urlpatterns = [
    url(r'^/(?P<id>[A-Za-z0-9-]+)$', view=views.ProvinceView.as_view()),
    url(r'^$', view=views.ProvinceView.as_view()),
]