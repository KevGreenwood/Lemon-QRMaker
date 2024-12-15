import io
import base64

from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, SquareModuleDrawer, CircleModuleDrawer, \
    RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.main import QRCode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import *

REAL_BLACK: tuple = (0, 0, 0)
FAKE_BLACK: tuple = (1, 0, 0)


class QRGenerator(QRCode):
    def __init__(self):
        super().__init__()
        self.use_gradiant: bool = False
        self.custom_eye_color: bool = False
        self.use_logo: bool = False
        self.inner_use_gradiant: bool = False
        self.outer_use_gradient: bool = False

        # Using StyledPilImage with pure black color as background cause that the whole QR Code turns fully black
        self.main_color: tuple = REAL_BLACK
        self.back_color: tuple = (255, 255, 255)
        self.alt_color: tuple = (0, 0, 255)
        self.main_color_inner_eyes: tuple = REAL_BLACK
        self.alt_color_inner_eyes: tuple = self.alt_color
        self.main_color_outer_eyes: tuple = REAL_BLACK
        self.alt_color_outer_eyes: tuple = self.alt_color

        self.data: str = ""
        self.logo_path: str = ""
        self.image_mask_path = ""

        self.colorMask_index: int = 0
        self.bodyDrawer_index: int = 0
        self.eyeDrawer_index: int = 0
        # box_size base: 37x37, so, just multiply by your desire number for scale your qr
        self.real_box_size: int = 10

        self.color_masks = {
            0: SolidFillColorMask,
            1: RadialGradiantColorMask,
            2: SquareGradiantColorMask,
            3: HorizontalGradiantColorMask,
            4: VerticalGradiantColorMask,
            5: ImageColorMask
        }
        self.shape_drawer = {
            0: SquareModuleDrawer(),
            1: GappedSquareModuleDrawer(),
            2: CircleModuleDrawer(),
            3: RoundedModuleDrawer(),
            4: VerticalBarsDrawer(),
            5: HorizontalBarsDrawer()
        }

        self.img = None
    
    def __build_qr(self):
        self.clear()
        self.add_data(self.data)
        self.make()
        self.get_colors_style()

    def get_colors_style(self):
        color_mask_class = self.color_masks.get(self.colorMask_index, None)
        self.back_color = FAKE_BLACK if self.back_color == REAL_BLACK else self.back_color
        body_draw_class = self.shape_drawer.get(self.bodyDrawer_index, None)
        eye_draw_class = self.shape_drawer.get(self.eyeDrawer_index, None)


        embed_image = self.logo_path if self.use_logo else None


        if self.use_gradiant and self.colorMask_index != 5:
            self.img = self.make_image(StyledPilImage, module_drawer=body_draw_class, eye_drawer=eye_draw_class, color_mask=color_mask_class(self.back_color, self.main_color, self.alt_color), embeded_image_path=embed_image)
        elif self.colorMask_index == 5:
            self.img = self.make_image(StyledPilImage, module_drawer=body_draw_class, eye_drawer=eye_draw_class, color_mask=ImageColorMask(self.back_color, color_mask_path=self.image_mask_path), embeded_image_path=embed_image)
        else:
            self.img = self.make_image(StyledPilImage, module_drawer=body_draw_class, eye_drawer=eye_draw_class, color_mask=SolidFillColorMask(self.back_color, self.main_color), embeded_image_path=embed_image)


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