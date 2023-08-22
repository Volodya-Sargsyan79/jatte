import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Room

@require_POST
def create_room(request, uuid):
    name = require_POST.get('name', '')
    url = require_POST.get('url', '')

    Room.objects.create(uuid=uuid, client=name, url=url)

    return JsonResponse({'message': 'room created'})