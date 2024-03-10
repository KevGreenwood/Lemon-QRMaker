import qrcode
import PIL
import io
import base64

class QRGenerator:
    def __init__(self):
        self.data = ""
        self.version = 0
        self.box_size = 0 # base: 29, so, just multiply by yout desire number for scale your qr 
        self.border = 0

        self.back_color = ""
        self.main_color = ""
        self.alt_color = ""

        self.logo_path = ""
        self.qr_path = ""
        self.preview = ""

    def generate(self):
        qr = qrcode.QRCode(
                            version=self.version, 
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=self.box_size,
                            border=self.border
                        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.main_color, back_color=self.back_color)

        byte_arr = io.BytesIO()
        img.save(byte_arr, format='JPEG')
        encoded_image = base64.b64encode(byte_arr.getvalue()).decode("utf-8")
        self.preview = encoded_image