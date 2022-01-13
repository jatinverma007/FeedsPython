from register import views as users_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import (
    UserSignupAPIView,LoginApiView
)

from Feeds.views import FeedsListApiView
urlpatterns = [
    # url('home/', users_views.home, name='home'),
    url(r'^register/$', UserSignupAPIView.as_view(), name='register'),
    url(r'^login/$', LoginApiView.as_view(), name='login'),
    url(r'^feeds/$', FeedsListApiView.as_view(), name='feeds'),
]