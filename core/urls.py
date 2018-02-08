from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^risk/all/', views.risk_list),
    url(r'^risk/(?P<pk>[0-9]+)/$', views.risk_detail),
    ]