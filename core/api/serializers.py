from rest_framework import serializers
from core.models import Application, Developer, Person, Platform, Publisher


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ["url", "application_name", "application_url", "release_date"]


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ["url", "developer", "developer_url"]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ["url", "person_name", "person_email"]


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ["url", "platform", "platform_url"]


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ["url", "publisher", "publisher_url"]
