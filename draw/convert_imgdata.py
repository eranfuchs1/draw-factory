from PIL import Image


canvas_width = 400
canvas_height = 300


def create_image(canvas_width=400, canvas_height=300):
    # return Image.new('RGB', (canvas_width, canvas_height), color = 'black')
    return Image.new('RGBA', (canvas_width, canvas_height), color='black')


def convert_imgdata(imgdata, img, canvas_width=400, canvas_height=300):
    idx = 0
    for j in canvas_width:
        for i in canvas_height:
            color = [imgdata[idx], imgdata[idx + 1],
                     imgdata[idx + 2], imgdata[idx + 3]]
            img.putpixel([j, i], color)
            idx += 4
    return img
