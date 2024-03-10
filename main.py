import qrcode
import PIL
import io
import base64

class QRGenerator:
    def __init__(self):
        self.data = ""
        self.version = None
        self.box_size = 0 # base: 33x33, so, just multiply by yout desire number for scale your qr 
        self.border = 0

        self.back_color = ""
        self.main_color = ""
        self.alt_color = ""

        self.logo_path = ""
        self.qr_path = ""
        self.prev = None
        self.preview = ""

    def generate_preview(self):
        qr = qrcode.QRCode(
                            version=self.version, 
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=self.box_size,
                            border=self.border
                        )
        qr.add_data(self.data)
        qr.make(fit=True)

        self.qr_path = qr.make_image(fill_color=self.main_color, back_color=self.back_color)
        self.prev = self.qr_path

        byte_arr = io.BytesIO()
        self.prev.save(byte_arr, format='JPEG')
        encoded_image = base64.b64encode(byte_arr.getvalue()).decode("utf-8")
        self.preview = encoded_image

    def generate(self, path):
        self.qr_path.save(f"{path}.png")

    def get_res(self):
        resolution = self.prev.size
        return resolution
