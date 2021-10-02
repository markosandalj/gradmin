from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.models import AnswerChoice, Matura, Problem, Question, Section
from skripte.models import Skripta
from .serializers import MaturaSerializer, ProblemSerializer, MaturaWithoutProblemsSerializer, SectionProblemsSerializer, SectionSerializer, SkriptaSectionsSerializer, SkriptaSerializer, UpdateQuestionSerializer
import json

# Create your views here.

# class MaturaApiView(generics.ListAPIView):
#     # queryset = Matura.objects.filter(pk=pk)
#     serializer_class = MaturaSerializer

#     def get_queryset(self):
#         if( self.kwargs.get('pk') ):
#             queryset = Matura.objects.filter(pk=self.kwargs.get('pk'))
#         else:
#             queryset = Matura.objects.all()
#         return queryset

# class MaturaWithoutProblemsApiView(generics.ListAPIView):
#     serializer_class = MaturaWithoutProblemsSerializer

#     def get_queryset(self):
#         kwargs_values = self.kwargs
#         arguments = {}
#         for k, v in kwargs_values.items():
#             if v:
#                 arguments[k] = v

#         if(len(arguments) > 0 ):
#             queryset = Matura.objects.filter(**arguments)
#         else:
#             queryset = Matura.objects.all()
#         return queryset


class SkriptaApiView(generics.ListAPIView):
    serializer_class = SkriptaSerializer

    def get_queryset(self):
        skripta = Skripta.objects.get(pk=self.kwargs.get('pk'))
        id = skripta.id
        name = skripta.name
        subject = skripta.subject
        sections = []
        for section in skripta.sections.all():
            problems = Problem.objects.filter(skripta=skripta, section=section)
            section_obj = {
                'id': section.id,
                'name': section.name,
                'problems': problems
            }
            sections.append(section_obj)

        queryset = [
            {
                'id': id,
                'name': name,
                'subject': subject,
                'sections': sections
            }
        ]
        return queryset

class SkriptaSectionProblemsApiView(generics.ListAPIView):
    serializer_class = SectionProblemsSerializer

    def get_queryset(self):
        skripta = Skripta.objects.get(pk=self.kwargs.get('skripta_id'))
        section = Section.objects.get(pk=self.kwargs.get('section_id'))
        problems = Problem.objects.filter(skripta=skripta, section=section)
        queryset = [{
            'order': section.order,
            'name': section,
            'problems': problems
        }]
        return queryset

class SkriptaSectionsApiView(generics.ListAPIView):
    serializer_class = SkriptaSectionsSerializer

    def get_queryset(self):
        queryset = Skripta.objects.filter(pk=self.kwargs.get('skripta_id'))
        return queryset


class UpdateQuestionApiView(APIView):
    serializer_class = UpdateQuestionSerializer

    def post(self, request, format=None):
        data = request.data
        if('questions' in data.keys()):
            for q in json.loads(data['questions']):
                question = Question.objects.get(id=int(q['id']))
                if( q['question_text'] != question.question_text):
                    question.question_text = q['question_text']
                    question.save(update_fields=['question_text'])
        if('answer_choices' in data.keys()):
            for ac in json.loads(data['answer_choices']):
                answer_choice = AnswerChoice.objects.get(id=int(ac['id']))
                if( ac['choice_text'] != answer_choice.choice_text):
                    answer_choice.choice_text = ac['choice_text']
                    answer_choice.save(update_fields=['choice_text'])

        return Response(status=status.HTTP_200_OK)