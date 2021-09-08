from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .convert_imgdata import ImageConverter


@api_view(['POST'])
@parser_classes([JSONParser])
def test_api_view(request, format=None):
    """
    A view that can accept POST requests with JSON content.
    """
    #print(request.data)
    img_converter = ImageConverter()
    img_converter.put_imgdata(request.data)
    image = img_converter.convert_to_image()
    image.show()
    return Response({'received data': request.data})

# Create your views here.


def test_html_view(request):
    return render(request, 'test.html')


'''
def test_api_view(request):
    if request.method == 'POST':
        #request.POST
        #each post, for now just print the
        #imgdata.
        for key in request.POST:
            print(key)
        #print(request.POST['data'])
        print(request.DATA)

    return HttpResponse('')
'''
