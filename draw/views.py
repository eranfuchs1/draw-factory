from django.shortcuts import render, HttpResponse, Http404
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


implement_menu_bar = True
if implement_menu_bar:
    implement_menu_bar_order_by = True 


@api_view(['POST'])
@parser_classes([JSONParser])
def test_api_view(request, drawing_tool, canvas_id=None):
    tool_model = DrawingTools.objects.get(tool=drawing_tool)
    img_converter = ImageConverter()
    img_converter.put_imgdata(request.data)
    image = img_converter.convert_to_image()
    if False:
        image.show()
    if tool_model.order == 1:
        canvas = Canvas.objects.create()
    elif canvas_id:
        canvas = Canvas.objects.get(id=canvas_id)
    else:
        last_tool = DrawingTools.objects.get(order=tool_model.order - 1)
        canvas = Canvas.objects.get(last_tool=last_tool)
    buffer = BytesIO()
    image.save(fp=buffer, format='PNG')
    content_file = ContentFile(buffer.getvalue())
    img_name = 'default.png'
    canvas.img = InMemoryUploadedFile(
        content_file,
        None,
        img_name,
        'image/png',
        content_file.tell,
        None)
    canvas.last_tool = tool_model
    canvas.in_use = False
    canvas.save()
    if False:
        return Response({'success': 'True'})
    return Response({'received data': request.data})


@api_view(['GET'])
@parser_classes([JSONParser])
def test_api_get_view(request, drawing_tool, using_canvas_id=None, using_in_use=None):
    tool_model = DrawingTools.objects.get(tool=drawing_tool)
    last_tool = DrawingTools.objects.get(order=tool_model.order - 1)
    img_converter = ImageConverter()
    if using_in_use == 'True':
        found = False
        for canvas_object in Canvas.objects.filter(last_tool=last_tool):
            if not canvas_object.in_use:
                img_converter.put_image(Image.open(canvas_object.img))
                canvas_object.in_use = True
                canvas_object.save()
                found = True
                image_object = canvas_object
                break
        if not found:
            return HttpResponse(Http404())
    else:
        image_object = list(Canvas.objects.filter(last_tool=last_tool))[-1]
        img_converter.put_image(Image.open(image_object.img))
    imgdata = img_converter.convert_to_imgdata()
    imgdata = img_converter.convert_list_to_dict(imgdata)
    if using_canvas_id == 'True':
        return Response({'canvas_id': image_object.id, 'imgdata': imgdata})
    return Response(imgdata)


def test_html_view(request, drawing_tool):
    if implement_menu_bar:
        drawing_tools = DrawingTools.objects.all()
        if implement_menu_bar_order_by:
            drawing_tools = drawing_tools.order_by('order')
    tool_model = DrawingTools.objects.get(tool=drawing_tool)
    tool_order = tool_model.order
    context = {
            'drawing_tool_order': tool_order,
            'drawing_tool': f'tools/{drawing_tool}.html',
            'drawing_tool_name': f'{drawing_tool}',
            'implement_conveyor_belt': 'True',
            'implement_machine_box': 'True',
            'implement_machine_box_right': 'True',
            'other_tool': 'tools/rectangles_tool.js',
            'implement_pop_by_position': 'True',
            }
    if implement_menu_bar:
        context['menu_bar_links_names'] = [drawing_tool.tool for drawing_tool in drawing_tools]
        context['implement_menu_bar'] = 'True'
        context['implement_flexbox'] = 'True'
        context['implement_menu_bar_main_style'] = 'False'
    if context['implement_pop_by_position'] == 'True':
        context['implement_pop_by_position_left_based'] = 'False'
    return render(request, 'canvas_styling_for_conveyor_belt.html', context=context)


def test_show_all_view(request):
    context = {}
    return render(request, 'show_all/index.html', context=context)

@api_view(['GET'])
@parser_classes([JSONParser])
def test_api_get_ids_view(request, drawing_tool=None):
    if drawing_tool:
        last_tool = DrawingTools.objects.get(tool=drawing_tool)
    else:
        last_tool = DrawingTools.objects.all().order_by('order').last()
    canvas_objects = Canvas.objects.filter(last_tool=last_tool)
    context = {'canvas_ids':[]}
    for index, canvas_object in enumerate(canvas_objects):
        context['canvas_ids'].append(canvas_object.id)
    return Response(context)