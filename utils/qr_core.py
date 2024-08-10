import io
import base64
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *


class QRGenerator:
    def __init__(self):
        self.qr = None # Instance of qrcode.QRCode
        self.version: int = None
        self.box_size: int = 50 # base: 33x33, so, just multiply by your desire number for scale your qr
        self.border: int = 4
        self.data: str = None
        self.use_logo: bool = False
        # Can be hex values or RGB Tuples   
        self.main_color: str | tuple = None
        self.back_color: str | tuple = None
        self.alt_color: tuple = None
        # Paths
        self.logo_path: str = None
        self.final_qr: str = None

        self.error_correction = None

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
            
            self.final_qr = self.qr.make_image(fill_color=self.main_color, back_color=self.back_color)


    def __adding_data(self) -> None:
        self.qr.add_data(self.data)
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
                self.final_qr = self.qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(self.back_color, self.main_color, self.alt_color))