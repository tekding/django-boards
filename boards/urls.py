from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^fcv$',views.home,name='home')
]

