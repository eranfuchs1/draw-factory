from django.urls import path
from .views import test_html_view


urlpatterns = [
    path('test_html/', test_html_view, name='test_html'),
]
