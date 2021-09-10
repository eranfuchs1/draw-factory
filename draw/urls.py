from django.urls import path
from .views import test_html_view, test_api_view, test_api_get_view


urlpatterns = [
    path('test_html/<str:drawing_tool>/', test_html_view, name='test_html'),
    path('test_api/<str:drawing_tool>/', test_api_view, name='test_api'),
    path('test_api_get/<str:drawing_tool>/', test_api_get_view, name='test_api_get'),
]
