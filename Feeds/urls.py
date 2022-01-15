from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from .views import (
    FeedsListApiView
)

urlpatterns = [
    # url(r'^feeds/$', FeedsListApiView.as_view(), name='feeds'),
]
