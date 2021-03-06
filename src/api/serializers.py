from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.expressions import F
from django.utils import tree
from rest_framework import serializers
from problems.models import AnswerChoice, CorrectAnswer, Matura, Problem, Question
from shopify_models.models import Page, Product
from skripte.models import Category, Equation, Razred, Section, SectionSection, Skripta, SkriptaSection, Subject
from cheatsheets.models import Cheatsheet, CheatsheetSeactionEquation, CheatsheetSection, CheatsheetTable, CheatsheetTableEquation, CheatsheetLayout
from media.models import PDF, SVG, Image, Video
from mature.models import Matura, MaturaSubject, Term, Year

from django.db.models.fields import IntegerField
from django.db.models.functions.comparison import Cast

## --------- BASE SERIALIZERS --------- ##
class ProuctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'handle')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'page_id', 'handle', 'title')

class EquationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equation
        fields = ('id', 'name', 'equation',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_dark')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'vimeo_id', 'vimeo_secondary_id', 'vimeo_view_url', 'vimeo_embed_url', 'vimeo_thumbnail_url', 'length')

class SVGSerializer(serializers.ModelSerializer):
    class Meta:
        model = SVG
        fields = ('id', 'image',)

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ('id', 'file',)

class AnswerChoiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = AnswerChoice
        fields = ('id', 'choice_text', 'images')

class CorrectAnswerSerializer(serializers.ModelSerializer):
    answer_choice = AnswerChoiceSerializer(many=False)
    images = ImageSerializer(many=True)

    class Meta:
        model = CorrectAnswer
        fields = ('id', 'answer_text', 'answer_choice', 'images')

class SubqestionSerializer(serializers.ModelSerializer):
    correct_answer = CorrectAnswerSerializer(many=True)
    answer_choices = AnswerChoiceSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Question
        fields =  ('id', 'question_text', 'correct_answer', 'answer_choices', 'images', )

class QuestionSerializer(serializers.ModelSerializer):
    subquestions = SubqestionSerializer(many=True, read_only=True)
    correct_answer = CorrectAnswerSerializer(many=True)
    answer_choices = AnswerChoiceSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Question
        fields =  ('id', 'question_text', 'subquestions', 'correct_answer', 'answer_choices', 'images' ) 

class SkriptaSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkriptaSection
        fields = ('id', 'section_order',)

class RazredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razred
        fields = ('id', 'name', )

class CategorySerialzier(serializers.ModelSerializer):
    razred = RazredSerializer(many=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'razred')

class SectionSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')
    section_order = SkriptaSectionSerializer(many=False, read_only=True)
    number_of_problems = serializers.SerializerMethodField('get_number_of_problems')
    category = CategorySerialzier(many=False, read_only=True)
    page = PageSerializer(many=False, read_only=True)
    icon = SVGSerializer(many=False, read_only=True)

    def get_number_of_problems(self, obj):
        section = obj
        problems = Problem.objects.filter(section=section)
        return len(problems)

    class Meta:
        model = Section
        fields = ('id', 'name', 'subject_name', 'section_order', 'number_of_problems', 'category', 'page', 'icon')

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'year',)

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('id', 'term',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

class MaturaSubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')

    class Meta:
        model = MaturaSubject
        fields = ('id', 'subject_name', 'level',)

class MaturaSerializer(serializers.ModelSerializer):
    term = TermSerializer(many=False)
    year = YearSerializer(many=False)
    subject = MaturaSubjectSerializer(many=False)
    product = ProuctSerializer(many=False)

    def get_number_of_problems(self, obj):
        matura = obj
        problems = Problem.objects.filter(matura=matura)
        return len(problems)
    
    class Meta:
        model = Matura
        fields = ('id', 'year', 'term', 'subject', 'product', 'file')

class ProblemSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)
    video_solution = VideoSerializer(many=False) 
    section = SectionSerializer(many=False)
    matura = MaturaSerializer(many=False)

    class Meta:
        model = Problem
        fields = ('id', 'name', 'number', 'approval', 'shop_availability', 'question', 'video_solution', 'section', 'matura',)


class SkriptaSerializer(serializers.ModelSerializer):
    subject = MaturaSubjectSerializer(many=False)

    class Meta:
        model = Skripta
        fields = ('id', 'name', 'subject',)

class CheatsheetSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Cheatsheet
        fields = ('id', 'name', 'subject')

class CheatsheetSectionSerializer(serializers.ModelSerializer):
    equations = serializers.SerializerMethodField('get_equations')

    def get_equations(self, instance):
        seaction_equations = CheatsheetSeactionEquation.objects.filter(cheatsheet_section__id = instance.id)
        equations = Equation.objects.filter(id__in = [seaction_equatio.equation.id for seaction_equatio in seaction_equations])
        response = EquationSerializer(equations, many=True).data
        return response

    class Meta:
        model = CheatsheetSection
        fields = ('name', 'decorator', 'equations')

class CheatsheetTableSerializer(serializers.ModelSerializer):
    equations = serializers.SerializerMethodField('get_equations')

    def get_equations(self, instance):
        table_equations = CheatsheetTableEquation.objects.filter(cheatsheet_table__id = instance.id)
        equations = Equation.objects.filter(id__in = [table_equation.equation.id for table_equation in table_equations])
        response = EquationSerializer(equations, many=True).data
        return response

    class Meta:
        model = CheatsheetTable
        fields = ('name', 'decorator', 'equations')

class CheatsheetLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheatsheetLayout
        fields = '__all__'


class CheatsheetFullViewSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)
    layout = CheatsheetLayoutSerializer(many=False)
    cheatsheet_sections = serializers.SerializerMethodField('get_cheatsheet_sections')
    cheatsheet_tables = serializers.SerializerMethodField('get_cheatsheet_tables')

    def get_cheatsheet_sections(self, instance):
        cheatsheet_sections = CheatsheetSection.objects.filter(cheatsheet__id = instance.id)
        response = CheatsheetSectionSerializer(cheatsheet_sections, many=True).data
        return response
    
    def get_cheatsheet_tables(self, instance):
        cheatsheet_tables = CheatsheetTable.objects.filter(cheatsheet__id = instance.id)
        response = CheatsheetTableSerializer(cheatsheet_tables, many=True).data
        return response

    class Meta:
        model = Cheatsheet
        fields = ('id', 'name', 'subject', 'cheatsheet_sections', 'cheatsheet_tables', 'layout')


## --------- FE MATURA SERIALIZERS --------- ##

class FEMaturaSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)
    term = TermSerializer(many=False)
    year = YearSerializer(many=False)
    subject = MaturaSubjectSerializer(many=False)

    class Meta:
        model = Matura
        fields = ('id', 'year', 'term', 'subject', 'problems',)



## --------- QR SKRIPTA SERIALIZERS --------- ##

class QRSkriptaProblemSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)
    video_solution = VideoSerializer(many=False)
    matura = MaturaSerializer(many=False) # needed for creation of QR codes

    class Meta:
        model = Problem
        fields = ('id', 'name', 'number', 'question', 'matura', 'video_solution')

class QRSkriptaSectionSerializer(serializers.ModelSerializer):
    problems = QRSkriptaProblemSerializer(many=True,read_only=True,)
    section_order = SkriptaSectionSerializer(many=False, read_only=True)
    equations = serializers.SerializerMethodField('get_equations')
    file = PDFSerializer(many=False, read_only=True)

    def get_equations(self, instance):
        equations = Equation.objects.filter(section__name = instance['name'])
        response = EquationSerializer(equations, many=True).data
        return response

    class Meta:
        model = Section
        fields = ('id', 'name', 'equations', 'problems', 'section_order', 'file')

class QRSkriptaSerializer(serializers.ModelSerializer):
    sections = QRSkriptaSectionSerializer(many=True, read_only=True)
    subject = MaturaSubjectSerializer(many=False)

    class Meta:
        model = Skripta
        fields = ('id', 'name', 'subject', 'sections')

class QRSkriptaListSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Skripta
        fields = ('id', 'name', 'sections', )




## --------- SHOPIFY-PAGE SERIALIZERS --------- ##

class ShopifyPageProblemSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)
    video_solution = VideoSerializer(many=False)
    matura = MaturaSerializer(many=False)
    section = SectionSerializer(many=False)
    question = QuestionSerializer(many=False, read_only=True)

    def get_equations(self, instance):
        response = EquationSerializer(instance.equations.all(), many=True).data
        return response

    class Meta:
        model = Problem
        fields = ('id', 'name', 'question',  'approval', 'shop_availability', 'video_solution', 'matura', 'section', 'equations',)

class ShopifyPageSkriptaSerializer(serializers.ModelSerializer):
    page = PageSerializer(many=False, read_only=True)
    
    class Meta:
        model = Skripta
        fields = ('id', 'name', 'label', 'label_short', 'page', )

class ShopifyPageSectionListSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')
    category = CategorySerialzier(many=False, read_only=True)
    page = PageSerializer(many=False, read_only=True)
    icon = SVGSerializer(many=False, read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'subject_name', 'category', 'page', 'icon', 'exclude')

class ShopifyPageSkriptaListSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField('get_sections')

    def get_sections(self, instance):
        sections = Section.objects.filter(skripta__in = [instance.id])
        response = ShopifyPageSectionListSerializer(sections.order_by('skriptasection__section_order'), many=True)
        return response.data

    class Meta:
        model = Skripta
        fields = ('id', 'name', 'label', 'sections', )


class ShopifyPageRelatedSectionSerializer(serializers.ModelSerializer):
    page = PageSerializer(many=False, read_only=True)
    icon = SVGSerializer(many=False, read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'page', 'icon')

class ShopifyPageSectionSerializer(serializers.ModelSerializer):
    problems = ShopifyPageProblemSerializer(many=True,read_only=True,)
    related_sections = serializers.SerializerMethodField('get_related_sections')
    
    def get_related_sections(self, instance):
        response = ShopifyPageRelatedSectionSerializer(instance.related_sections.all(), many=True).data
        return response

    class Meta:
        model = Section
        fields = ('id', 'name', 'problems', 'related_sections',)





## --------- SHOPIFY-PRODUCT SERIALIZERS --------- ##

class ShopifyProductSkriptaSerializer(serializers.ModelSerializer):
    file = PDFSerializer(many=False)
    page = PageSerializer(many=False, read_only=True)

    class Meta:
        model = Skripta
        fields = ('id', 'name', 'file', 'page')

class ShopifyProductProblemSerializer(serializers.ModelSerializer):
    equations = serializers.SerializerMethodField('get_equations')
    video_solution = VideoSerializer(many=False) 
    section = SectionSerializer(many=False)
    question = QuestionSerializer(many=False, read_only=True)

    def get_equations(self, instance):
        response = EquationSerializer(instance.equations.all(), many=True).data
        return response

    class Meta:
        model = Problem
        fields = ('id', 'approval', 'number', 'shop_availability', 'question', 'video_solution', 'section', 'equations', )

class ShopifyProductMaturaSerializer(serializers.ModelSerializer):
    problems = serializers.SerializerMethodField('get_problems')
    term = TermSerializer(many=False)
    year = YearSerializer(many=False)
    subject = MaturaSubjectSerializer(many=False)
    file = PDFSerializer(many=False)
    skripta = ShopifyProductSkriptaSerializer(many=False)

    def get_problems(self, instance):
        response = ShopifyProductProblemSerializer(Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(matura=instance).order_by('number_field', 'name'), many=True)
        return response.data

    class Meta:
        model = Matura
        fields = ('id', 'year', 'term', 'subject', 'file', 'skripta', 'problems',)

## --------- POST SERIALIZERS --------- ##

class UpdateQuestionSerializer(serializers.ModelSerializer):
    answer_choices = AnswerChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ('question_text', 'answer_choices', )