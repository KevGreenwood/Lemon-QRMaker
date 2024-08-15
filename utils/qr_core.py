import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *
import io
import base64

import qrcode.main


class QRGenerator(qrcode.main.QRCode):
    def __init__(self):
        super().__init__(box_size=50)
        # box_size base: 33x33, so, just multiply by your desire number for scale your qr
        self.data: str = None
        self.use_logo: bool = False
        self.use_gradiant: bool = False
        self.main_color: tuple = (0, 0, 0)
        self.back_color: tuple = (255, 255, 255)
        self.alt_color: tuple = (0, 0, 255)
        self.logo_path: str = None
        self.error_correction: int = 0
        self.img = None
    
    def __build_qr(self):
        self.clear()
        self.add_data(self.data)
        self.make()
        if self.use_logo:
            self.img = self.make_image(StyledPilImage, color_mask=SolidFillColorMask(self.back_color, self.main_color), 
                module_drawer = SquareModuleDrawer(),
                embeded_image_path = self.logo_path)
        else:
            self.img = self.make_image(StyledPilImage, color_mask=SolidFillColorMask(self.back_color, self.main_color))
    
    def get_error_correction(self, index):
        match index:
            case 0:
                self.error_correction = 1
            case 1:
                self.error_correction = 0
            case 2:
                self.error_correction = 3
            case 3:
                self.error_correction = 2

    def get_colors_style(self, index):
        if self.use_gradiant:
            match index:
                case 0:
                    self.img = self.make_image(StyledPilImage, color_mask=RadialGradiantColorMask(self.back_color, self.main_color, self.alt_color))
                case 1:
                    self.img = self.make_image(StyledPilImage, color_mask=SquareGradiantColorMask(self.back_color, self.main_color, self.alt_color))
                case 2:
                    self.img = self.make_image(StyledPilImage, color_mask=HorizontalGradiantColorMask(self.back_color, self.main_color, self.alt_color))
                case 3:
                    self.img = self.make_image(StyledPilImage, color_mask=VerticalGradiantColorMask(self.back_color, self.main_color, self.alt_color))
    
    def generate_preview(self):
        self.__build_qr()
        byte_arr = io.BytesIO()
        self.img.save(byte_arr, format='PNG')
        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")

    def generate_final(self, path) -> None:
        self.img.save(f"{path}.png")

    def get_res(self):
        return f"{self.img.size[0]} x {self.img.size[1]}"
    

"""
class QRGenerator:
    def __init__(self):
        self.version: int = None
        self.error_correction: int = 0
        self.box_size: int = 50 # base: 33x33, so, just multiply by your desire number for scale your qr
        self.border: int = 4

        self.data: str = None
        self.main_color: tuple = (0, 0, 0)
        self.back_color: tuple = (255, 255, 255)
        self.alt_color: tuple = (0, 0, 255)
        self.use_logo: bool = False
        
        # Paths
        self.logo_path: str = None
        self.final_qr

        

        self.qr = None # Instance of qrcode.QRCode

    def __building_qr(self):
        if self.use_logo:
            self.qr = qrcode.QRCode(
                version=self.version, 
                error_correction=self.error_correction,
                box_size=self.box_size,
                border=self.border
            )
            self.__adding_data()
            self.final_qr = self.qr.make_image(
                image_factory = StyledPilImage, 
                module_drawer = SquareModuleDrawer(),
                embeded_image_path = self.logo_path
            )
        else:
            self.qr = qrcode.QRCode(
                version=self.version, 
                box_size=self.box_size,
                border=self.border
            )
            self.__adding_data()
            
            self.final_qr = self.qr.make_image(image_factory=StyledPilImage, 
                                                   color_mask=SolidFillColorMask(self.back_color, self.main_color))


    def __adding_data(self) -> None:
        add_data(self.data)
        self.qr.make(fit=True)

    def generate_preview(self) -> str:
        self.__building_qr()
        byte_arr = io.BytesIO()
        self.final_qr.save(byte_arr, format='PNG')
        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")

    def generate_final(self, path) -> None:
        self.final_qr.save(f"{path}.png")

    def get_res(self) -> str:
        return f"{self.final_qr.size[0]} x {self.final_qr.size[1]}"
    
    def get_error_correction(self, index):
        match index:
            case 0:
                self.error_correction = qrcode.constants.ERROR_CORRECT_L
            case 1:
                self.error_correction = qrcode.constants.ERROR_CORRECT_M
            case 2:
                self.error_correction = qrcode.constants.ERROR_CORRECT_Q
            case 3:
                self.error_correction = qrcode.constants.ERROR_CORRECT_H
    
    def get_gradiant_style(self, index):
        match index:
            case 0:
                self.final_qr = self.qr.make_image(image_factory=StyledPilImage, 
                                                   color_mask=RadialGradiantColorMask(self.back_color, self.main_color, self.alt_color))
"""