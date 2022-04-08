from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ name filed for testing Apiviews"""

    name = serializers.CharField(max_length=10)
