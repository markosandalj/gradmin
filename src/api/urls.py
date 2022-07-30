from django.urls import path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

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
    CheatsheetsFullView,
)

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

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
    path('shopify_product/m,atura/<int:matura_id>', ShopifyProductMaturaView.as_view())
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]