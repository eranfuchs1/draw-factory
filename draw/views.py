from django.shortcuts import render

# Create your views here.
def test_html_view(request):
    return render(request, 'test.html')
