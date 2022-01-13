from Feeds.models import Feeds
from rest_framework import serializers

class FeedsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Feeds
        fields = [
            'id',
            'profile',
            'feed_type',
            'title',
            'desc',
            'link',
        ]