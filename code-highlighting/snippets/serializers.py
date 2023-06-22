from .helper import LANGUAGE_CHOICES, STYLE_CHOICES
from .models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            "id", 
            "title", 
            "code", 
            "id", 
            "linenos", 
            "language", 
            "style"
        )