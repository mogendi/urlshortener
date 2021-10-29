from django.shortcuts import render, redirect
from django.views.generic import View
from api.serializers import UrlSerializer
from rest_framework import viewsets
from api.models import Url
from rest_framework.decorators import api_view

class UrlViewSet(viewsets.ModelViewSet):
    queryset         = Url.objects.all()
    serializer_class = UrlSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def redirect_to_origin(r, id):
    try:
        org = Url.objects.get(url_id=id)
        org.inc()
    except Url.DoesNotExist:
        return redirect("/new_url/")
    return redirect(org.url_actual)

class UrlGenForm(View):

    def get(self, r):
        return render(r, 'urls.html')