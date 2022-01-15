from register import views as users_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import (
    UserSignupAPIView,LoginApiView
)

from Feeds.views import (
    FeedsListApiView, FeedsCreateApiView, FeedsUpdateApiView
)
urlpatterns = [
    # url('home/', users_views.home, name='home'),
    url(r'^register/$', UserSignupAPIView.as_view(), name='register'),
    url(r'^login/$', LoginApiView.as_view(), name='login'),
    url(r'^feeds/$', FeedsListApiView.as_view(), name='feeds'),
    url(r'^feeds/create/$', FeedsCreateApiView.as_view(), name='feeds-create'),
    url(r'^feeds/(?P<pk>[0-9]+)/$', FeedsUpdateApiView.as_view()),
]