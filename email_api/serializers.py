from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    name = serializers.CharField()
    education = serializers.CharField()
    contact = serializers.CharField()
    address = serializers.CharField()
    project_idea = serializers.CharField()
    screenshot = serializers.ImageField()
    recipients = serializers.ListField(
    child=serializers.EmailField()
    )
