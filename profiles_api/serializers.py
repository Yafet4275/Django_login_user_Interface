from rest_framework import serializers

class Helloserilizers(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    