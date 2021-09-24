from django.urls import path
from .views import test_html_view, test_api_view, test_api_get_view, test_api_get_ids_view, test_show_all_view


urlpatterns = [
    path('test_html/<str:drawing_tool>/', test_html_view, name='test_html'),
    path('test_api/<str:drawing_tool>/', test_api_view, name='test_api'),
    path('test_api/<str:drawing_tool>/<int:canvas_id>/', test_api_view, name='test_api_canvas_id'),
    path('test_api_get/<str:drawing_tool>/<str:using_canvas_id>/<str:using_in_use>/', test_api_get_view, name='test_api_get'),
    path('test_api_get/<str:drawing_tool>/<str:using_canvas_id>/<str:using_in_use>/<int:canvas_id>/', test_api_get_view, name='test_api_get_by_id'),
    path('test_api_get_ids/<str:drawing_tool>', test_api_get_ids_view, name='test_api_get_ids'),
    path('test_api_get_ids/', test_api_get_ids_view, name='test_api_get_ids_last_tool'),
    path('test_html_show_all/', test_show_all_view, name='test_html_show_all'),
    path('test_html_show_all/<int:page_number>', test_show_all_view, name='test_html_show_all_pages'),
]
