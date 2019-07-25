from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'im/(\d+)',views.image,name = 'singleImage'),
    url(r'^$',views.account,name = 'account'),
    url(r'^search/',views.search,name = 'search'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^account/(?P<username>[-_\w.]+)/edit/$',views.profile_edit,name='profile_edit'),
    url(r'^post/$',views.post_picture,name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
