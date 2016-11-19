from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import ReceiveSentence, MorseCombination

@api_view(exclude_from_schema = True)
@permission_classes((AllowAny,))
def index(request):
    return Response({'urls': [{'alphabet': 'http://127.0.0.1:8000/api/alphabet'}]})

@api_view(['GET', 'POST'], exclude_from_schema = True)
@permission_classes((AllowAny,))
def alphabet(request):
    if request.method == 'POST':

        if 'sentence' in request.data:
            sentence = request.data['sentence']
            receive_sentence = ReceiveSentence(sentence = sentence)
            receive_sentence.save()

            words = list(sentence.lower())
            result = {}

            combinations = []
            for word in words:
                if word == ' ':
                    morse = ''
                else:
                    try:
                        morse = MorseCombination.objects.filter(word = word)[0].combination
                    except Exception as e:
                        return Response({"error": "Unsupport word. Only alphabet", "sentence": request.data['sentence']})

                word_dictionary = {}
                word_dictionary['morse'] = morse
                word_dictionary['word'] = word

                combinations.append(word_dictionary)

            result['result'] = combinations
            result['sentence'] = sentence

            return Response(result)

        return Response({"error": "Please format", "format": {"sentence": "Hello"}, "data": request.data})
    return Response({"error": "Not allowed method"})
