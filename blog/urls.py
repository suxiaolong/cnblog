from django.urls import path, re_path
from blog import views
from django.views.static import serve
from cnblog import settings

urlpatterns = [
    re_path('^login/$', views.login, name='login'),
    re_path('^get_validCode/$', views.get_validCode, name='get_validCode'),
    re_path('^index/$', views.index, name='index'),
]
