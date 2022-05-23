import cv2
from html5lib import serialize
from pdf2image import convert_from_path, convert_from_bytes
import sys
import base64
import numpy as np
from rest_framework import viewsets
from rest_framework.response import Response
from PIL import Image
from django.db.models.fields import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.http import FileResponse
from django.core.files.base import File
import requests
import json
import time
import os
from pathlib import Path


from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from weasyprint import HTML, CSS
import cloudinary.uploader
import cloudinary

from cheatsheets.models import (
    Cheatsheet,
    CheatsheetSection,
    CheatsheetTable,
    CheatsheetLayout
)

from media.models import (
    PDF,
    Image
)
from mature.models import (
    MaturaSubject,
    Subject
)
from problems.models import (
    AnswerChoice, 
    Matura, 
    Problem, 
    Question, 
    Section
)
from skripte.models import (
    Equation, 
    Skripta, 
    SkriptaSection
)
from .serializers import (
    PDFSerializer,
    FEMaturaSerializer, 
    MaturaSerializer, 
    ProblemSerializer, 
    QRSkriptaListSerializer, 
    QRSkriptaSectionSerializer, 
    QRSkriptaSerializer, 
    ShopifyPageSectionSerializer, 
    ShopifyPageSkriptaListSerializer, 
    ShopifyProductMaturaSerializer, 
    UpdateQuestionSerializer,
    ImageSerializer,
    SubjectSerializer,
    SectionSerializer,
    SkriptaSerializer,
    CheatsheetSerializer,
    CheatsheetFullViewSerializer,
    CheatsheetLayoutSerializer
)


# Create your views here.
class AllSkriptasListApiView(generics.ListAPIView):
    serializer_class = SkriptaSerializer    

    def get_queryset(self):
        skriptas = Skripta.objects.all()
        queryset = skriptas
        
        return queryset


class AllSectionsListApiView(generics.ListAPIView):
    serializer_class = SectionSerializer    

    def get_queryset(self):
        sections = Section.objects.all()
        queryset = sections
        
        return queryset

class AllSubjectsListApiView(generics.ListAPIView):
    serializer_class = SubjectSerializer    

    def get_queryset(self):
        subjects = Subject.objects.all()
        queryset = subjects
        
        return queryset

class AllMaturasListApiView(generics.ListAPIView):
    serializer_class = MaturaSerializer

    def get_queryset(self):
        maturas = Matura.objects.all()
        queryset = maturas
        
        return queryset

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
        problems = Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(matura=matura).order_by('number_field', 'name')
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
            'section_order': skripta_section.section_order,
            'file': skripta.file
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



## --------- CHEATSHEETS VIEWS --------- ##
class CheatsheetsListView(generics.ListAPIView):
    serializer_class = CheatsheetSerializer

    def get_queryset(self):
        queryset = Cheatsheet.objects.all()

        return queryset

class CheatsheetsFullView(viewsets.ViewSet):

    def retrieve(self, request, id=None):
        cheatsheet = Cheatsheet.objects.get(pk=self.kwargs.get('id'))
        serializer = CheatsheetFullViewSerializer(cheatsheet)
        layout_serializer = CheatsheetLayoutSerializer(CheatsheetLayout.objects.all(), many=True)
        data = { **serializer.data, 'layouts': layout_serializer.data}
        return Response(data)


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

class PrintSkripta(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            skripta = Skripta.objects.get(pk = data['id'])


            html_string = json.loads(data['html'])
            pdf_file_path = Path(settings.BASE_DIR / 'tmp.pdf')
            html_file_path = Path(settings.BASE_DIR / 'tmp.html')
            

            with open(html_file_path, 'w') as html_file:
                html_file.write(html_string)
            

            html = HTML(filename=html_file_path, encoding="UTF-8")
            print(html, pdf_file_path, Path(settings.STATICFILES_DIRS[0] / 'assets/print.css'))
            pdf_file = html.write_pdf(pdf_file_path, stylesheets=[Path(settings.STATICFILES_DIRS[0] / 'assets/print.css')])

            
            if(skripta.file != None):
                pdf_model = PDF.objects.get(pk = skripta.file.id)
                pdf_model.file.save(skripta.name + '.pdf', File(open(pdf_file_path, 'rb')))
                serializer = PDFSerializer(pdf_model, many=False)
                data = json.dumps(serializer.data)
            else:
                pdf_model = PDF(name=skripta.name, file=File(open(pdf_file_path, 'rb')))
                pdf_model.save()
                skripta.file = pdf_model
                skripta.save()
                serializer = PDFSerializer(pdf_model, many=False)
                data = json.dumps(serializer.data)

            html_file_path.unlink()
            pdf_file_path.unlink()

            return Response(status=status.HTTP_200_OK, data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={ 'error': sys.exc_info()[0] })


class ProblemsImporterUpdateView(APIView):
    def post(self, request, format = None):
        data = json.loads( request.data['data'] )
        # print(data)
        matura = data['matura'][0] if data['matura'] else None
        skripta = data['skripta'][0] if data['skripta'] else None
        subject = data['subject'][0] if data['subject'] else None
        section = data['section'][0] if data['section'] else None
        subject_label = Subject.objects.get(pk = int(subject)).name if subject else None
        matura_level = Matura.objects.get(pk = int(matura)).subject.level if matura else 0
        level_label = matura_level if matura_level != '0' else ''
        matura_godina = Matura.objects.get(pk = int(matura)).year.year if matura else None
        matura_rok = Matura.objects.get(pk = int(matura)).term.term if matura else None
        new_questions = []
        new_answer_choices = []
        new_problems = []
        errors = []

        for problem in data['problems']:
            try:
                try:
                    new_question = Question.objects.create(
                        question_text = problem['question']['text']
                    )
                    new_questions.append(new_question)
                except:
                    print('Question error: ', sys.exc_info()[0])
                    errors.append({ 'Question error: ': sys.exc_info()[0] })

                try: 
                    for choice in problem['answer_choices']:
                        new_answer_choice = AnswerChoice.objects.create(
                            choice_text = choice['text'],
                            question = new_question
                        )
                        new_answer_choices.append(new_answer_choice)

                    try:
                        new_problem = Problem.objects.create(
                            name=f"{subject_label}{level_label} - {matura_godina}. {matura_rok}, { problem['number'] }",
                            number = problem['number'],
                            matura = Matura.objects.get(pk = int(matura)) if matura else None,
                            subject = Subject.objects.get(pk = int(subject)) if subject else None,
                            section = Section.objects.get(pk = int(section)) if section else None,
                            question = new_question
                        )
                        related_skripta = Skripta.objects.get(pk = int(skripta)) if skripta else None,

                        if(related_skripta):
                            new_problem.skripta.set([int(skripta), ])
                            
                        new_problems.append(new_problem)
                    except:
                        print('Problem error: ', sys.exc_info()[0])
                        errors.append({ 'Problem error: ', sys.exc_info()[0] })
                except:
                    print('Choice error: ', sys.exc_info()[0])
                    errors.append({ 'Choice error: ': sys.exc_info()[0] })

                try:
                    image = Image.objects.get(id = int(problem['image_id']))
                    image.delete()
                    cloudinary.uploader.destroy(problem['image_public_id'], invalidate=True)
                except:
                    print('Image error: ', sys.exc_info()[0])
                    errors.append({ 'Image error: ': sys.exc_info()[0] })

            except:
                print('Krep krepalo', sys.exc_info()[0])
        
        try:
            return Response(status=status.HTTP_200_OK, data=errors)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProblemsImporterView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            file = data['file'].read()
            images = convert_from_bytes(file)
            response_data = []

            for i, image in enumerate(images):
                try:
                    image = np.asarray(image)
                    image = getEdges(image)
                    response_data += getAllProblemsArea(image)
                    
                except:
                    print("Slika je krepala. Error: {err}".format(err = sys.exc_info()[0]))

            return Response(status=status.HTTP_200_OK, data=response_data)
        except:
            print("Not gonna happen! Error: {err}".format(i=i, err = sys.exc_info()[0]))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=json.dumps({ 'error': sys.exc_info()[0] }))




def getMathpixResponse(image):
    try:
        cv2.imwrite('tmp.png', image)
        image_uri = "data:image/jpg;base64," + base64.b64encode(open('tmp.png', "rb").read()).decode()
        r = requests.post(
            "https://api.mathpix.com/v3/text",
            data=json.dumps({'src': image_uri, 'include_line_data': True} ),
            headers={
                "app_id": "marko_sandalj23_gmail_com_cd23e6", 
                "app_key": "b56dcf2eb92232d1b905",
                "Content-type": "application/json"
            }
        )
        print("Image", json.loads(r.text)["request_id"])
        try:
            image_object = Image()
            image_object.image = File(open("tmp.png", 'rb'))
            image_object.save()
            serializer = ImageSerializer(image_object, many = False)
            data = {
                'image': serializer.data,
                'mathpix_response': json.loads(r.text)
            }
        except:
            print('Image se ne da spremiti u bazu. Error: {err}'.format(err = sys.exc_info()[0]))

        os.remove('tmp.png')
        return data if data else None
    except:
        print('Mathpix response je krepao. Error: {err}'.format(err = sys.exc_info()[0]))


def getEdges(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    blur = cv2.GaussianBlur(thresh_inv,(1,1),0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mask = np.ones(image.shape[:2], dtype="uint8") * 255
    
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w*h>1000:
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

    image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    
    return image


def getSingleProblemArea(img, cnt, contours, i):
    cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
    mask = np.zeros_like(img) # Create mask where white is what we want, black otherwise
    cv2.drawContours(mask, contours, i,(255,255,255), -1) # Draw filled contour in mask
    out = np.zeros_like(img) # Extract out the object and place into output image
    out[mask == 255] = img[mask == 255]
    
    x, y, w, h = cv2.boundingRect(cnt)
    out = out[y:y+h,x:x+w]

    return out



def getAllProblemsArea(img):
    data = []
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 150000.0]
    i=len(contours)-1

    for cnt in contours[::-1]:
        area = cv2.contourArea(cnt)
        image = getSingleProblemArea(img, cnt, contours, i)
        response = getMathpixResponse(image)
        if(response):
            data.append(response)
        i-=1

    return data