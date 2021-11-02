from django.db.models.fields import IntegerField
from django.shortcuts import render
from mature.models import MaturaSubject
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.models import AnswerChoice, Matura, Problem, Question, Section
from skripte.models import Equation, Skripta, SkriptaSection
from .serializers import FEMaturaSerializer, MaturaSerializer, ProblemSerializer, QRSkriptaListSerializer, QRSkriptaSectionSerializer, QRSkriptaSerializer, SectionSerializer, ShopifyPageSectionSerializer, ShopifyPageSkriptaListSerializer, ShopifyProductMaturaSerializer, UpdateQuestionSerializer
import json
from django.db.models.functions import Cast

# Create your views here.

class MaturaListApiView(generics.ListAPIView):
    serializer_class = MaturaSerializer

    def get_queryset(self):
        subject = MaturaSubject.objects.get(pk = self.kwargs.get('subject_id'))
        maturas = Matura.objects.filter(subject=subject)
        queryset = maturas
        
        return queryset

class MaturaApiView(generics.ListAPIView):
    serializer_class = FEMaturaSerializer

    def get_queryset(self):
        matura = Matura.objects.get(pk = self.kwargs.get('matura_id'))
        problems = Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(matura=matura).order_by('number_field', 'question')
        queryset = [{
            'id': matura.id,
            'term': matura.term,
            'year': matura.year,
            'subject': matura.subject,
            'problems': problems
        }]
        return queryset
    




## --------- QR SKRIPTA VIEWS --------- ##

class QRSkriptaListView(generics.ListAPIView):
    serializer_class = QRSkriptaListSerializer

    def get_queryset(self):
        queryset = Skripta.objects.filter(pk=self.kwargs.get('skripta_id'))
        return queryset

class QRSkriptaView(generics.ListAPIView):
    serializer_class = QRSkriptaSerializer

    def get_queryset(self):
        skripta = Skripta.objects.get(pk=self.kwargs.get('pk'))
        id = skripta.id
        name = skripta.name
        subject = skripta.subject
        sections = []
        for section in skripta.sections.all():
            problems = Problem.objects.filter(skripta=skripta, section=section)
            equations = Equation.objects.filter(section=section)
            skripta_section = SkriptaSection.objects.get(section=section, skripta=skripta)
            section_obj = {
                'id': section.id,
                'name': section.name,
                'equations': equations,
                'problems': problems,
                'section_order': skripta_section.section_order
            }
            sections.append(section_obj)

        queryset = [{
                'id': id,
                'name': name,
                'subject': subject,
                'sections': sections
            }]
        return queryset

class QRSkriptaSectionView(generics.ListAPIView):
    serializer_class = QRSkriptaSectionSerializer

    def get_queryset(self):
        skripta = Skripta.objects.get(pk=self.kwargs.get('skripta_id'))
        section = Section.objects.get(pk=self.kwargs.get('section_id'))
        problems = Problem.objects.filter(skripta=skripta, section=section)
        equations = Equation.objects.filter(section=section)
        skripta_section = SkriptaSection.objects.get(section=section, skripta=skripta)

        queryset = [{
            'id': section.id,
            'name': section.name,
            'equations': equations,
            'problems': problems,
            'section_order': skripta_section.section_order
        }]
        return queryset




## --------- SHOPIFY-PAGE VIEWS --------- ##

class ShopifyPageSectionView(generics.ListAPIView):
    serializer_class = ShopifyPageSectionSerializer

    def get_queryset(self):
        queryset = Section.objects.filter(pk=self.kwargs.get('section_id'))
        return queryset

class ShopifyPageSkriptaListView(generics.ListAPIView):
    serializer_class = ShopifyPageSkriptaListSerializer

    def get_queryset(self):
        queryset = Skripta.objects.filter(pk=self.kwargs.get('skripta_id'))
        return queryset





## --------- SHOPIFY-PRODUCT VIEWS --------- ##

class ShopifyProductMaturaView(generics.ListAPIView):
    serializer_class = ShopifyProductMaturaSerializer

    def get_queryset(self):
        queryset = Matura.objects.filter(pk=self.kwargs.get('matura_id'))
        return queryset


## --------- POST VIEWS --------- ##

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
        if('problems' in data.keys()):
            for pr in json.loads(data['problems']):
                problem = Problem.objects.get(id=int(pr['id']))
                if( pr['approval'] != problem.approval):
                    problem.approval = pr['approval']
                    problem.save(update_fields=['approval'])

        # if('images' in data.keys()):
            # TODO upload images
        return Response(status=status.HTTP_200_OK)