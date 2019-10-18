from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
     url(r'^image$',views.new_image,name = 'new'),
]