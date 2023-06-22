from .helper import LANGUAGE_CHOICES, STYLE_CHOICES
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ReadOnlyField
)

class SnippetSerializer(HyperlinkedModelSerializer):
    owner = ReadOnlyField(source="owner.username")
    highlight = HyperlinkedIdentityField(
        view_name="snippet-highlight",
        format="html"
    )

    class Meta:
        model = Snippet
        fields = (
            "url",
            "id",
            "highlight", 
            "title", 
            "code", 
            "id", 
            "linenos", 
            "language", 
            "style",
            "owner",
        )

class UserSerializer(HyperlinkedModelSerializer):
    snippets = HyperlinkedRelatedField(
        many=True,
        view_name="snippet-detail",
        read_only=True
    )

    class Meta:
        model = User
        fields = ("url", "id", "username", "snippets")
