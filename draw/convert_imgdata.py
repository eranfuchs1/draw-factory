from PIL import Image


class ListConverter:
    def convert_dict_to_list(self, obj):
        idx = 0
        answer = []
        while str(idx) in obj:
            answer.append(obj[str(idx)])
            idx += 1
        return answer

    def convert_list_to_dict(self, obj):
        answer = {}
        for index, value in enumerate(obj):
            answer[str(index)] = value
        return answer


class ImageConverter(ListConverter):
    def __init__(self, canvas_width=400, canvas_height=300, image=None, imgdata=None):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.put_imgdata(imgdata)
        self.put_image(image)

    def put_imgdata(self, imgdata):
        self.imgdata = imgdata
        self.clean_imgdata()

    def clean_imgdata(self):
        if type(self.imgdata) == type(dict()):
            self.imgdata = self.convert_dict_to_list(self.imgdata)

    def put_image(self, image):
        self.image = image

    def convert(self):
        return [self.convert_to_image(), self.convert_to_imgdata()] if self.imgdata and self.image else self.convert_to_image() if self.imgdata else self.convert_to_imgdata() if self.image else None

    def convert_to_image(self):
        if self.imgdata == None:
            return None
        idx = 0
        image = self.create_image()
        print(len(self.imgdata))
        for i in range(self.canvas_height):
            for j in range(self.canvas_width):
                color = (self.imgdata[idx], self.imgdata[idx + 1],
                         self.imgdata[idx + 2], self.imgdata[idx + 3])
                image.putpixel([j, i], color)
                idx += 4
        return image

    def convert_to_imgdata(self):
        if not self.image:
            return None
        imgdata = self.create_imgdata()
        idx = 0
        for i in range(self.canvas_height):
            for j in range(self.canvas_width):
                color = self.image.getpixel((j, i))
                for index, value in enumerate(color):
                    imgdata[idx + index] = value
                idx += 4
        return imgdata

    def create_image(self):
        return Image.new('RGBA', (self.canvas_width, self.canvas_height), color='black')

    def create_imgdata(self):
        imgdata = [0 for _ in range(self.canvas_width*self.canvas_height*4)]
        return imgdata
