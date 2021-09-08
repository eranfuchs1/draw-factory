from django.urls import path
from .views import test_html_view, test_api_view


urlpatterns = [
    path('test_html/', test_html_view, name='test_html'),
    path('test_api/', test_api_view, name='test_api'),
]
