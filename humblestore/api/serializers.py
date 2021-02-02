from rest_framework import serializers
from humblestore.models import HumbleBundle, HumbleItem


class HumbleBundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HumbleBundle
        fields = ["url", "bundle_name", "bundle_url"]


class HumbleItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HumbleItem
        fields = [
            "url",
            "application",
            "developer",
            "publisher",
            "bundle",
            "redemption_platform",
            "code_expiration_date",
            "is_gift",
            "claimed_by",
            "date_claimed",
        ]
