import random
from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import Words


class WordsSerializator(serializers.ModelSerializer):

    class Meta:
        model = Words
        fields = ["pk","word","gender"]


class RandomWord(APIView):
    def get(self,*args,**kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordsSerializator(random_word, many=False)
        return Response(serialized_random_word.data )

class NextWord(APIView):
    def get(self,request,pk,format=None):
        word = Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        ser_word = WordsSerializator(word, many=False)
        return Response(ser_word.data)
