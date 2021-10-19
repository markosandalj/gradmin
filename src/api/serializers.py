from django.db import models
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from problems.models import AnswerChoice, CorrectAnswer, Matura, Problem, Question
from skripte.models import Section, Skripta, Subject
from media.models import Image, Video
from mature.models import Matura, MaturaSubject, Term, Year


# MEDIA BASE SERIALIZERS 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image',)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'vimeo_id', 'vimeo_view_url', 'vimeo_embed_url',)


#  ---------------------------------------------------


# PROBLEMS BASE SERILIZERS
class AnswerChoiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = AnswerChoice
        fields = ('id', 'choice_text', 'images')

class CorrectAnswerSerializer(serializers.ModelSerializer):
    answer_choice = AnswerChoiceSerializer(many=False)

    class Meta:
        model = CorrectAnswer
        fields = ('id', 'answer_text', 'answer_choice',)

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

class SectionSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')
    number_of_problems = serializers.SerializerMethodField('get_number_of_problems')

    def get_number_of_problems(self, obj):
        section = obj
        problems = Problem.objects.filter(section=section)
        return len(problems)

    class Meta:
        model = Section
        fields = ('id', 'name', 'subject_name', 'shopify_page_id', 'order', 'number_of_problems')

#  ---------------------------------------------------


# MATURA BASE SERIALIZERS
class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'year',)

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('id', 'term',)

class MaturaSubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')

    class Meta:
        model = MaturaSubject
        fields = ('id', 'subject_name', 'level',)

class MaturaSerializer(serializers.ModelSerializer):
    term = TermSerializer(many=False)
    year = YearSerializer(many=False)
    subject = MaturaSubjectSerializer(many=False)
    number_of_problems = serializers.SerializerMethodField('get_number_of_problems')

    def get_number_of_problems(self, obj):
        matura = obj
        problems = Problem.objects.filter(matura=matura)
        return len(problems)
    
    class Meta:
        model = Matura
        fields = ('id', 'year', 'term', 'subject', 'number_of_problems')

class ProblemSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)
    video_solution = VideoSerializer(many=False) 
    section = SectionSerializer(many=False)
    matura = MaturaSerializer(many=False)

    class Meta:
        model = Problem
        fields = ('id', 'name', 'number', 'approval', 'shop_availability', 'question', 'video_solution', 'section', 'matura',)

# MATURA VIEW SERILEZERS
class MaturaProblemsSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)
    term = TermSerializer(many=False)
    year = YearSerializer(many=False)
    subject = MaturaSubjectSerializer(many=False)

    class Meta:
        model = Matura
        fields = ('id', 'year', 'term', 'subject', 'problems',)


#  ---------------------------------------------------


# SKRIPTA BASE SERIALIZERS
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name',)

# SKRIPTA VIEW SERIALIZERS
class SectionProblemsSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True,read_only=True,)
    class Meta:
        model = Section
        fields = ('id', 'name', 'problems', 'order', )

class ShopifyPageProblemsSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)
    video_solution = VideoSerializer(many=False)
    class Meta:
        model = Problem
        fields = ('id', 'name', 'question', 'video_solution' )

class SkriptaSerializer(serializers.ModelSerializer):
    sections = SectionProblemsSerializer(many=True, read_only=True)
    problems = ProblemSerializer(many=True,read_only=True,)
    subject = MaturaSubjectSerializer(many=False)
    class Meta:
        model = Skripta
        fields = ('id', 'name', 'subject', 'sections', 'problems')

class SkriptaSectionsSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Skripta
        fields = ('id', 'name', 'sections', )

class UpdateQuestionSerializer(serializers.ModelSerializer):
    answer_choices = AnswerChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ('question_text', 'answer_choices', )