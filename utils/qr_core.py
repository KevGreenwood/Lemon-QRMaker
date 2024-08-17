import PIL.Image
import PIL.ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *
import io
import base64
from qrcode.main import QRCode
import PIL
from PIL import Image, ImageDraw

class QRGenerator(QRCode):
    def __init__(self):
        super().__init__()
        # box_size base: 37x37, so, just multiply by your desire number for scale your qr
        
        self.data: str = None
        self.use_logo: bool = False
        self.use_gradiant: bool = False
        self.custom_eye_color: bool = False
        
        # Using StyledPilImage with pure black color as background cause that the whole QR Code turns fully black
        self.REAL_BLACK: tuple = (0, 0, 0)
        self.FAKE_BLACK: tuple = (1, 0, 0)
        self.main_color: tuple = self.REAL_BLACK
        self.back_color: tuple = (255, 255, 255)
        self.alt_color: tuple = (0, 0, 255)

        self.main_color_inner_eyes: tuple = (255, 0, 0)
        self.alt_color_inner_eyes: tuple = self.alt_color

        self.main_color_outter_eyes: tuple = (255, 100, 50)
        self.alt_color_outter_eyes: tuple = self.alt_color
        
        self.logo_path: str = None
        self.img = None

        self.index: int = 0

        self.real_box_size: int = None
    
    def __build_qr(self):
        self.clear()
        self.add_data(self.data)
        self.make()
        self.get_colors_style()

    def style_inner_eyes(self, img):
        img_size = img.size[0]
        eye_size = 70 #default
        quiet_zone = 40 #default
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle((60, 60, 90, 90), fill=255) #top left eye
        draw.rectangle((img_size-90, 60, img_size-60, 90), fill=255) #top right eye
        draw.rectangle((60, img_size-90, 90, img_size-60), fill=255) #bottom left eye
        return mask

    def style_outer_eyes(self, img):
        img_size = img.size[0]
        eye_size = 70 #default
        quiet_zone = 40 #default
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle((40, 40, 110, 110), fill=255) #top left eye
        draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255) #top right eye
        draw.rectangle((40, img_size-110, 110, img_size-40), fill=255) #bottom left eye
        draw.rectangle((60, 60, 90, 90), fill=0) #top left eye
        draw.rectangle((img_size-90, 60, img_size-60, 90), fill=0) #top right eye
        draw.rectangle((60, img_size-90, 90, img_size-60), fill=0) #bottom left eye  
        return mask  

    def get_colors_style(self):
        color_masks = {
            0: SolidFillColorMask,
            1: RadialGradiantColorMask,
            2: SquareGradiantColorMask,
            3: HorizontalGradiantColorMask,
            4: VerticalGradiantColorMask
        }

        color_mask_class = color_masks.get(self.index, None)
        self.back_color = self.FAKE_BLACK if self.back_color == self.REAL_BLACK else self.back_color
        
        embed_image = self.logo_path if self.use_logo else None

        if self.use_gradiant:
            self.img = self.make_image(StyledPilImage, color_mask=color_mask_class(self.back_color, self.main_color, self.alt_color), embeded_image_path=embed_image)
        else:
            self.img = self.make_image(StyledPilImage, color_mask=SolidFillColorMask(self.back_color, self.main_color), embeded_image_path=embed_image)
        
        if self.custom_eye_color:
            inner_eyes = self.make_image(StyledPilImage, color_mask=SolidFillColorMask(self.back_color, self.main_color_inner_eyes))
            outter_eyes = self.make_image(StyledPilImage, color_mask=SolidFillColorMask(self.back_color, self.main_color_outter_eyes))
            inner_eye_mask = self.style_inner_eyes(self.img)
            outter_eye_mask = self.style_outer_eyes(self.img)

            temp = Image.composite(inner_eyes, self.img, inner_eye_mask)
            self.img = Image.composite(outter_eyes, temp, outter_eye_mask)

    def get_draw_style(self):
        pass

    def generate_preview(self):
        self.box_size = 10
        self.__build_qr()
        byte_arr = io.BytesIO()
        self.img.save(byte_arr, format='WEBP')
        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")

    def generate_final(self, path) -> None:
        self.box_size = self.real_box_size
        self.__build_qr()
        self.img.save(f"{path}.png")

    def get_res(self):
        return f"{int(self.img.size[0]/10 * self.real_box_size)} x {int(self.img.size[1]/10 * self.real_box_size)}"