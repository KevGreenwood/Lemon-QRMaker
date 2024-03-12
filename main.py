import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *

import io
import base64

class QRGenerator:
    def __init__(self):
        self.qr = None
        self.version = None
        self.box_size = 50 # base: 33x33, so, just multiply by yout desire number for scale your qr
        self.border = 4
        self.data = ""
        self.use_logo = False    
        self.main_color = None
        self.back_color = None
        self.alt_color = None
        self.logo_path = ""
        self.final_qr = ""
        self.preview = ""

    def building_qr(self):
        self.qr = qrcode.QRCode(
                    version=self.version, 
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=self.box_size,
                    border=self.border
                    )
        self.qr.add_data(self.data)
        self.qr.make(fit=True)
        if self.use_logo:
            self.final_qr = self.qr.make_image(
                image_factory = StyledPilImage, 
                module_drawer = SquareModuleDrawer(),
                embeded_image_path=self.logo_path
            )
        else:
            self.final_qr = self.qr.make_image(fill_color=self.main_color, back_color=self.back_color)

    def generate_preview(self):
        self.building_qr()
        byte_arr = io.BytesIO()
        self.final_qr.save(byte_arr, format='PNG')
        encoded_image = base64.b64encode(byte_arr.getvalue()).decode("utf-8")
        self.preview = encoded_image

    def generate_final(self, path):
        self.final_qr.save(f"{path}.png")

    def get_res(self):
        resolution = self.final_qr.size
        return resolution