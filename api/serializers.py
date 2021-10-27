from api.models import Url
from django.db.models import fields
from rest_framework import serializers

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Url
        fields = ['url_actual','url_id']