from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .convert_imgdata import ImageConverter
from .models import Canvas, DrawingTools
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image


@api_view(['POST'])
@parser_classes([JSONParser])
def test_api_view(request, drawing_tool):
    """
    A view that can accept POST requests with JSON content.
    """
    # print(request.data)
    tool_model = DrawingTools.objects.get(tool=drawing_tool)
    img_converter = ImageConverter()
    img_converter.put_imgdata(request.data)
    image = img_converter.convert_to_image()
    image.show()
    if tool_model.order == 1:
        canvas = Canvas.objects.create()
    else:
        last_tool = DrawingTools.objects.get(order=tool_model.order - 1)
        canvas = Canvas.objects.get(last_tool=last_tool)
    buffer = BytesIO()
    image.save(fp=buffer, format='PNG')
    content_file = ContentFile(buffer.getvalue())
    #canvas.img = image
    img_name = 'default.png'
    canvas.img = InMemoryUploadedFile(
        content_file,
        None,
        img_name,
        'image/png',
        content_file.tell,
        None)
    canvas.last_tool = tool_model
    canvas.save()
    return Response({'received data': request.data})


@api_view(['GET'])
@parser_classes([JSONParser])
def test_api_get_view(request, drawing_tool):
    tool_model = DrawingTools.objects.get(tool=drawing_tool)
    last_tool = DrawingTools.objects.get(order=tool_model.order - 1)
    img_converter = ImageConverter()
    img_converter.put_image(Image.open(list(Canvas.objects.filter(last_tool=last_tool))[-1].img))
    imgdata = img_converter.convert_to_imgdata()
    imgdata = img_converter.convert_list_to_dict(imgdata)
    return Response(imgdata)
# Create your views here.


def test_html_view(request, drawing_tool):
    context = {'drawing_tool': f'tools/{drawing_tool}.html', 'drawing_tool_name': f'{drawing_tool}'}
    return render(request, 'test.html', context=context)


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
