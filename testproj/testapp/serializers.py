from rest_framework import serializers
from .models import *
import json
from .views import *


class Dropdown1Serializer001(serializers.ModelSerializer):

    class Meta:
        model = Dropdown1
        fields = "__all__"

class Dropdown2Serializer001(serializers.ModelSerializer):

    class Meta:
        model = Dropdown2
        fields = "__all__"

class Dropdown3Serializer001(serializers.ModelSerializer):

    class Meta:
        model = Dropdown3
        fields = "__all__"                