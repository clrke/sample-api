from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import Message

def messages(request):
    if request.method == 'GET':
        return JsonResponse([message.serialize() for message in Message.objects.all()], safe=False)
    else:
        data = request.POST
        message = Message(author=data['author'], content=data['content'])
        message.save()
        return JsonResponse(message.serialize(), safe=False)

def message(request, id):
    if request.method == 'GET':
        return JsonResponse(Message.objects.get(id=id).serialize(), safe=False)
    else:
        data = request.POST
        message = Message.objects.get(id=id)

        message.author = data['author']
        message.content = data['content']

        message.save()

        return JsonResponse(message.serialize(), safe=False)

