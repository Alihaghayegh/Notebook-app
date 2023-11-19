from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


# Get all of the notes
@api_view(['GET'])
def note_collection(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


# Get one note by primary key
@api_view(['GET'])
def note_element(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NoteSerializer(Note)
        return Response(serializer.data)
