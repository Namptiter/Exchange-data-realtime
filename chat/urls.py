from django.conf.urls import url

from . import views,views_auth

urlpatterns = [
    url(r'^$', views.chat_index, name='chat_index'),
    # url used to process the xmlhttprequests done by nodejs socket.io
    url(r'^save_message/$', views.save_message, name='chat_save_message'),
    url(r'^save_img/$', views.save_img, name='img'),
    url(r'^save_file/$', views.save_file, name='file'),

    url(r'^login/$', views_auth.loginn, name='login'),
    url(r'^register/$', views_auth.register, name='register'),
    url(r'^postregister/$', views_auth.postregister),
    url(r'^postlogin/$', views_auth.postlogin),
    url(r'^logout/$', views_auth.logoutt),
]