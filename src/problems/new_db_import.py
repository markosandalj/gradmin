# from mature.models import MaturaSubject
# from problems.models import AnswerChoice, CorrectAnswer, Problem, Question, Section, Matura, Subject, Term, Video, Year

# from pathlib import Path 
import pathlib
import json
import vimeo
import requests
import time
from bs4 import BeautifulSoup
from problems.models import Problem
from shopify_models.models import Product, Template

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
        name = subject + level_label + ' - skripta za dr??avnu maturu'
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
                    skripta_id = getSkripta(zad, subject, level)
                    getProblem(name, number, matura_id, question_id, subject_id, section_id, video_id, skripta_id)
    print('Import ending!')

importProblems('Matematika', 'gradivaB', 'B')

def getTemplate(template_suffix):
    try:
        new_template = Template.objects.get(
            template_suffix=template_suffix
        )
        return new_template.id
    except:
        new_template = Template(
            template_suffix=template_suffix
        )
        new_template.save()
        return new_template.id
    

def importShopifyPages():
    base_url = 'https://msandalj23.myshopify.com'
    headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
    pages_url = '/admin/api/2021-10/pages.json?limit=250'
    url = base_url + pages_url
    response = requests.get(url, headers=headers)
    pages = response.json()['pages']
    for page in pages:
        status = 'hidden' if page['published_at'] == None else 'active'
        new_page = Page(
            page_id=page['id'],
            title=page['title'],
            handle=page['handle'],
            template=Template.objects.get(id=getTemplate(page['template_suffix'])),
            graphql_api_id=page['admin_graphql_api_id'],
            status=status
        )
        new_page.save()
        try:
            update_section = Section.objects.get(shopify_page_id=page['id'])
            update_section.page = new_page
            update_section.save()
            print('ima')
        except:
            print('nema')



def importShopifyProducts():
    base_url = 'https://msandalj23.myshopify.com'
    headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
    pages_url = '/admin/api/2021-10/pages.json?limit=250'
    url = base_url + pages_url
    response = requests.get(url, headers=headers)
    pages = response.json()['pages']
    for page in pages:
        status = 'hidden' if page['published_at'] == None else 'active'
        new_page = Page(
            page_id=page['id'],
            title=page['title'],
            handle=page['handle'],
            template=Template.objects.get(id=getTemplate(page['template_suffix'])),
            graphql_api_id=page['admin_graphql_api_id'],
            status=status
        )
        new_page.save()
        try:
            update_section = Section.objects.get(shopify_page_id=page['id'])
            update_section.page = new_page
            update_section.save()
            print('ima')
        except:
            print('nema')

def importEquations():
    filepath = str(pathlib.Path().resolve()) + '/problems/eq.json'
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for section in data['sections']:
            if('z-gpg_' in section):
                for k, v in data['sections'][section].items():
                    if(k == 'blocks'):
                        for key, value in data['sections'][section][k].items():
                            if(value['type'] and value['type'] == 'equation'):
                                equation = value['settings']['equation'] if len(value['settings']['equation']) > 0 else '??TA JE OVO??'
                                equation_label = value['settings']['equation_label'] if len(value['settings']['equation_label']) > 0 else 'POPUNITI!'
                                if(equation_label != 'POPUNITI!' or equation != '??TA JE OVO??'):
                                    try: 
                                        section_obj = Section.objects.get(page__handle = section.replace('z-gpg_', ''))
                                    except:
                                        section_obj = None
                                    new_eq_obj = Equation(
                                        name = equation_label,
                                        equation = equation,
                                        description = equation_label,
                                        subject = Subject.objects.get(name='Matematika'),
                                    )
                                    new_eq_obj.save()
                                    new_eq_obj.section.set([section_obj, ])



def fetchVideoLegths():
    c = vimeo.VimeoClient(
        token='efe0a81055184db54700aa97ec9aa821',
        key='8e5f364f348c8c12ab10a8a3d48e35461a1e55fb',
        secret='zQHi4Z9WAalZ6LPUPP9lybCu5utepNl5mHtvL1QEnYpR/sgsKLFsC5Xvj/hMopJf9T0jJGfNHuWFTutePS7dGmZ8pRg1n3cVxf+RQOSRt0Kyf3eotVkWglaWmhX34UQn'
    )
    videos = Video.objects.all()
    for video in videos:
        if(video.vimeo_id != None):
            if(video.length == None):
                try:
                    response = c.get("https://api.vimeo.com/me/videos/" + str(video.vimeo_id) )
                    data = response.json()
                    duration = data['duration']
                    video.length = duration
                    video.save()
                    time.sleep(0.5)
                except:
                    print('1. Nes je krepalo:', video.vimeo_id)
            if(video.vimeo_secondary_id == None):
                try:
                    response = c.get("https://api.vimeo.com/me/videos/" + str(video.vimeo_id) )
                    data = response.json()
                    secondary_id = data['link'].replace('https://vimeo.com/', '').split('/')[1]
                    video.vimeo_secondary_id = secondary_id
                    video.save()
                    time.sleep(0.5)
                except:
                    print('2. Nes je krepalo:', video.vimeo_id)
            if(video.vimeo_embed_url == None):
                try:
                    response = c.get("https://api.vimeo.com/me/videos/" + str(video.vimeo_id) )
                    data = response.json()
                    print(data['embed']['html'] )
                    iframe = data['embed']['html']  
                    soup = BeautifulSoup(iframe, 'html.parser')
                    tag = soup.find_all('iframe')[0]
                    video.vimeo_embed_url = tag['src']
                    video.save()
                    time.sleep(0.5)
                except: 
                    print('3. Nes je krepalo:', video.vimeo_id)
            if(video.vimeo_view_url == None):
                



def deleteUslessVideoObjects():
    videos = Video.objects.all()
    for video in videos:
        try:
            problem = Problem.objects.get(video_solution=video)
        except:
            print(video.id)
            video.delete()


def importShopifyProducts():
    base_url = 'https://msandalj23.myshopify.com'
    headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
    products_url = '/admin/api/2021-10/products.json?limit=250'
    url = base_url + products_url
    response = requests.get(url, headers=headers)
    products = response.json()['products']
    for product in products:
        try:
            new_product = Product.object.get(product_id = product['id'])
            # product_id = product.id,
            # title = product.title,
            # vendor = product.vendor,
        except:
            print(product)
            status = 'draft' if product['published_at'] == None else 'active'
            new_product = Product(
                product_id = product['id'],
                title = product['title'],
                vendor = product['vendor'],
                type = product['product_type'],
                handle = product['handle'],
                graphql_api_id = product['admin_graphql_api_id'],
                status = status
            )
            new_product.save()


def replaceProductIdsWithProductModels():
    maturas = Matura.objects.all()
    for matura in maturas:
        try:
            matura.product = Product.objects.get(product_id = matura.shopify_product_id)
            matura.save()
        except:
            print(matura)