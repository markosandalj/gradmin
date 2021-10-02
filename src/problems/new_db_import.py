from mature.models import MaturaSubject
from problems.models import AnswerChoice, CorrectAnswer, Problem, Question, Section, Matura, Subject, Term, Video, Year
from openpyxl import load_workbook

# from pathlib import Path 
import pathlib
import json
import requests

from skripte.models import Skripta

def getName(zad, subject, level = 0):
    matura_godina = int("20" + zad["matura_godina"])
    matura_rok = zad["matura_rok"]
    matura_br_zad = zad["tekst_zadatka"].split(' ')[0]
    level_label = ' ' + level if level != 0 else ''
    name=f'{subject}{level_label} - {matura_godina}. {matura_rok}, {matura_br_zad}'
    print('Name:', name)
    return name

def getNumber(zad):
    br_zad = zad["tekst_zadatka"].split(' ')[0]
    print('Number:', br_zad)
    return str(br_zad)

def getMatura(zad, subject, level = 0):
    matura_godina = int("20" + zad["matura_godina"])
    matura_rok = zad["matura_rok"]
    try:
        new_matura=Matura.objects.get(
            year=Year.objects.get(year=matura_godina),
            term=Term.objects.get(term=matura_rok),
            subject=MaturaSubject.objects.get(subject__name=subject, level = level),
        )
        return new_matura.id
    except:
        new_matura = Matura(
            year=Year.objects.get(year=matura_godina),
            term=Term.objects.get(term=matura_rok),
            subject=MaturaSubject.objects.get(subject__name=subject, level = level),
        )
        new_matura.save()
        return new_matura.id

def getQuestion(zad):
    q_text = zad['tekst_zadatka']
    try:
        new_q = Question.objects.get(
            question_text=q_text
        )
        return int(new_q.id)
    except:
        new_q = Question(
            question_text=q_text
        )
        new_q.save()
        return int(new_q.id)

def getCorrectAnswer(zad):
    if(zad['tocan_odgovor'] != ''):
        try:
            new_correct_ans = CorrectAnswer(
                answer_text=zad['tocan_odgovor'],
                question=Question.objects.get(
                    id = getQuestion(zad)
                ),
            )
            new_correct_ans.save()
        except:
            print('Somethin went wrong.')
    else:
        try:
            new_correct_ans = CorrectAnswer(
                answer_choice = AnswerChoice.objects.filter(
                    question=Question.objects.get(id = getQuestion(zad)),
                )[int(zad['tocan_odgovor_zaokruzivanje'])-1],
                question=Question.objects.get(
                    id = getQuestion(zad)
                )
            )
            new_correct_ans.save()
        except: 
            print( 'A: ---> ' + Question.objects.get(id = getQuestion(zad)).question_text )

def getAnswerChoices(zad):
    answers = [
        zad['odgovor_a'],
        zad['odgovor_b'],
        zad['odgovor_c'],
        zad['odgovor_d']
    ]
    for ans in answers:
        if(ans != ''):
            try:
                new_ans_choice = AnswerChoice(
                    choice_text = ans[3:len(ans)],
                    question=Question.objects.get(
                             id = getQuestion(zad)
                        ),
                )
                new_ans_choice.save()
            except:
                print('Somethin went wrong')

def getSubject(zad, subject):
    print('Subject:', subject)
    new_subject = Subject.objects.get(
        name=str(subject),
    )
    return int(new_subject.id)

def getSection(zad):
    if(zad["naziv_gradiva"] != 'None'):
        print('Section:', str(zad["naziv_gradiva"]))
        new_section = Section.objects.get(
            name = str(zad["naziv_gradiva"])
        )
        return int(new_section.id)
    else:
        return None

def getVideoSolution(zad, subject, level):
    if(zad['vimeo_id'] != 'None'):
        try:
            new_video = Video.objcts.get(
                name = getName(zad, subject, level),
                vimeo_id = int(zad['vimeo_id'])
            )
            return int(new_video.id)
        except:
            new_video = Video(
                name = getName(zad, subject, level),
                vimeo_id = int(zad['vimeo_id'])
            )
            new_video.save()
            return int(new_video.id)
    else:
        return None

def getSkripta(zad, subject, level):
    level_label = ' ' + level if level != 0 else ''
    new_skripta = Skripta.objects.get(
        name = subject + level_label + ' - skripta za državnu maturu'
    )
    return int(new_skripta.id)

def getProblem(name, number, matura_id, question_id, subject_id, section_id, video_id, skripta_id):
    video_solution = Video.objects.get(id = video_id) if video_id != None else None
    section = Section.objects.get(id = section_id) if section_id != None else None
    try: 
        new_problem = Problem.objects.get(
            name = name,
            number = number,
            matura = Matura.objects.get(id = matura_id),
            question = Question.objects.get(id = question_id),
            subject = Subject.objects.get(id = subject_id),
            section = section,
            video_solution = video_solution,
        )
    except:
        new_problem = Problem(
            name = name,
            number = number,
            matura = Matura.objects.get(id = matura_id),
            question = Question.objects.get(id = question_id),
            subject = Subject.objects.get(id = subject_id),
            section = section,
            video_solution = video_solution,
        )
        new_problem.save()
        new_problem.skripta.set([Skripta.objects.get(id = skripta_id)])

def importProblems(subject, filename, level = 0):
    print('Import starting!')
    filepath = str(pathlib.Path().resolve()) + '/problems/'+ filename + '.json'
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for gradivo in data:
            for zad in data[gradivo]:
                if(zad['matura_godina'].lower() != 'x' and zad['matura_godina'].lower() != 'medicina'):
                    name = getName(zad, subject, level)
                    number = getNumber(zad)
                    matura_id = getMatura(zad, subject, level)
                    question_id = getQuestion(zad)
                    getAnswerChoices(zad)
                    getCorrectAnswer(zad)
                    subject_id = getSubject(zad, subject)
                    section_id = getSection(zad)
                    video_id = getVideoSolution(zad, subject, level)
                    skripta_id = getSkripta(zad, subject)
                    getProblem(name, number, matura_id, question_id, subject_id, section_id, video_id, skripta_id)
    print('Import ending!')

importProblems('Matematika', 'gradiva copy', 'A')