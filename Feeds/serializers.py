from Feeds.models import Comments, Feeds
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

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
	    model = Comments
fields = [
            'comment'
            ]

