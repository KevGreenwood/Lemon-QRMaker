import io
import base64
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *


class QRGenerator:
    def __init__(self):
        self.qr = None # Instance of qrcode.QRCode
        self.version = None
        self.box_size = 50 # base: 33x33, so, just multiply by your desire number for scale your qr
        self.border = 4
        self.data = ""
        self.use_logo = False
        # Can be hex values or RGB Tuples   
        self.main_color = None
        self.back_color = None
        self.alt_color = None
        # Paths
        self.logo_path = ""
        self.final_qr = ""

    def _building_qr(self):
        if self.use_logo:
            self.qr = qrcode.QRCode(
                version=self.version, 
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=self.box_size,
                border=self.border
            )
            self._adding_data()
            self.final_qr = self.qr.make_image(
                image_factory = StyledPilImage, 
                module_drawer = SquareModuleDrawer(),
                embeded_image_path=self.logo_path
            )
        else:
            self.qr = qrcode.QRCode(
                version=self.version, 
                box_size=self.box_size,
                border=self.border
            )
            self._adding_data()
            self.final_qr = self.qr.make_image(fill_color=self.main_color, back_color=self.back_color)

    def _adding_data(self):
        self.qr.add_data(self.data)
        self.qr.make(fit=True)

    def generate_preview(self):
        self._building_qr()
        byte_arr = io.BytesIO()
        self.final_qr.save(byte_arr, format='PNG')
        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")

    def generate_final(self, path):
        self.final_qr.save(f"{path}.png")

    def get_res(self):
        return f"{self.final_qr.size[0]} x {self.final_qr.size[1]}"