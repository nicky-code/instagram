from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/new_image$',views.new_image,name = 'new_image'),
    url(r'^new/profile$',views.new_profile,name = 'profile'),
    url(r'^myProfile$',views.myProfile,name = 'myProfile'),
    url(r'^search/',views.search_users, name = 'searchs'),
    url(r'^comment/(\d+)/$', views.add_comment, name='comment'),
    url(r'^likes/(?P<id>\d+)',views.likes,name ='like'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    