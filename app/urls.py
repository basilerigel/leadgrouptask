from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^drinks/$', views.DrinkList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
]
