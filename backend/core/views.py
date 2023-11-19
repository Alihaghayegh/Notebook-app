from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Note
from .serializers import NoteSerializer


# Get all the notes
@api_view(['GET', 'POST'])
def note_collection(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'title': request.data.get('title'),
                'author': request.user.pk,
                'content': request.data.get('content')
                }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get one note by primary key
@api_view(['GET'])
def note_element(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
