from django.urls import path

from .views import (
    MaturaApiView, 
    MaturaListApiView, 
    QRSkriptaListView, 
    QRSkriptaSectionView, 
    QRSkriptaView, 
    ShopifyPageSectionView, 
    ShopifyPageSkriptaListView, 
    ShopifyProductMaturaView, 
    UpdateQuestionApiView, 
    PrintSkripta,
    ProblemsImporterView,
    AllMaturasListApiView,
    AllSubjectsListApiView,
    AllSectionsListApiView,
    AllSkriptasListApiView,
    ProblemsImporterUpdateView,
    CheatsheetsListView,
    CheatsheetsFullView
)

urlpatterns = [
    # path('maturas/', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<int:pk>', MaturaApiView.as_view()),
    # path('maturas/<str:subject__name>', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<str:subject__name>/<str:year__year>', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<str:subject__name>/<str:year__year>/<str:term__term>', MaturaWithoutProblemsApiView.as_view()),
    path('cheatsheets/list', CheatsheetsListView.as_view()),
    path('cheatsheets/<int:id>', CheatsheetsFullView.as_view({'get': 'retrieve'})),
    path('question/update', UpdateQuestionApiView.as_view()),
    path('problems_importer', ProblemsImporterView.as_view()),
    path('problems_importer/update', ProblemsImporterUpdateView.as_view()),
    path('skripta/print', PrintSkripta.as_view()),
    path('skripta/<int:skripta_id>/list', QRSkriptaListView.as_view()),
    path('skripta/<int:pk>', QRSkriptaView.as_view()),
    path('skripta/<int:skripta_id>/<int:section_id>', QRSkriptaSectionView.as_view()),
    path('section/all', AllSectionsListApiView.as_view()),
    path('subject/all', AllSubjectsListApiView.as_view()),
    path('matura/all', AllMaturasListApiView.as_view()),
    path('skripta/all', AllSkriptasListApiView.as_view()),
    path('matura/<int:matura_id>', MaturaApiView.as_view()),
    path('matura/<int:subject_id>/list', MaturaListApiView.as_view()),
    path('shopify_page/section/list/<int:skripta_id>', ShopifyPageSkriptaListView.as_view()),
    path('shopify_page/section/<int:section_id>', ShopifyPageSectionView.as_view()),
    path('shopify_product/matura/<int:matura_id>', ShopifyProductMaturaView.as_view())
]