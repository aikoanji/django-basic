from django.conf.urls import url
from src.city import views
urlpatterns = [
    url(r'^(?P<id>[A-Za-z0-9-]+)$', view=views.CityView.as_view()),
    url(r'^$', view=views.CityView.as_view()),
]