import io
import base64
from qrcode.main import QRCode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import (
    SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask,
    HorizontalGradiantColorMask, VerticalGradiantColorMask, ImageColorMask
)
from qrcode.image.styles.moduledrawers import (
    GappedSquareModuleDrawer, SquareModuleDrawer, CircleModuleDrawer,
    RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
)


REAL_BLACK: tuple = (0, 0, 0)
# Using StyledPilImage with pure black color as background causes the whole QR code to turn fully black
FAKE_BLACK: tuple = (1, 0, 0)

class QRGenerator(QRCode):
    """A class to generate QR codes with customizable styles, colors, and embedded logos."""
    def __init__(self):
        super().__init__()
        self.use_logo: bool = False
        self.use_gradiant: bool = False
        #self.custom_eye_color: bool = False
        #self.inner_use_gradiant: bool = False
        #self.outer_use_gradient: bool = False
        
        self.back_color: tuple = (255, 255, 255)
        self.main_color: tuple = REAL_BLACK
        self.alt_color: tuple = (0, 0, 255)
        #self.main_color_inner_eyes: tuple = REAL_BLACK
        #self.alt_color_inner_eyes: tuple = self.alt_color
        #self.main_color_outer_eyes: tuple = REAL_BLACK
        #self.alt_color_outer_eyes: tuple = self.alt_color

        self.data: str = ""
        self.logo_path: str = ""
        self.img_fill_path = ""

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
    """
        def build_data(self, data_type: str, **kwargs):
        formats = {
            "url": lambda: kwargs.get("url", ""),
            "plain text": lambda: kwargs.get("text", ""),
            "mail": lambda: f"mailto:{kwargs.get('email')}?subject={kwargs.get('subject')}&body={kwargs.get('msg')}",
            "phone": lambda : f"tel:{kwargs.get('phone')}",
            "sms": lambda: f"SMSTO:{kwargs.get('phone')}:{kwargs.get('msg')}",
            "whatsapp": lambda: f"https://wa.me/{kwargs.get('phone')}/?text={kwargs.get('msg')}",
            "mecard": lambda: f"MECARD:N:{kwargs.get('lastname')},{kwargs.get('name')};NICKNAME:{kwargs.get('nick')};TEL:{kwargs.get('work_phone')};TEL:{kwargs.get('priv_phone')};TEL:{kwargs.get('phone')};EMAIL:{kwargs.get('email')};BDAY:{self.birthday};URL:{url_txt.value}NOTE:{filled_txt.value};ADR:,,{street_txt.value},{city_txt.value},{state_txt.value},{zip_txt.value},{country_txt.value};;",
            "map": lambda: f"https://maps.google.com/local?q={kwargs.get('latitude')},{kwargs.get('longitude')}",
            "wifi": lambda: f"WIFI:S:{ssid_txt.value};T:{wifi_encrypt};P:{pass_txt.value};H:{network_hide};;",
            "event": lambda: f"BEGIN:VEVENT\nUID:{title_txt.value}\nORGANIZER:{organizer_txt.value}\nLOCATION:{location_txt.value}\nDTSTART:{self.start_datetime}\nDTEND:{self.end_datetime}\nSUMMARY:{summary_txt.value}\nEND:VEVENT",
            "app": lambda: f"market://details?id={app_txt.value}",
            "favorite": lambda: f"MEBKM:TITLE:{title_txt.value};URL:{kwargs.get("url")};;",
            "paypal": lambda: f"https://www.paypal.com/cgi-bin/webscr?business={mail_txt.value}&cmd=_xclick&currency_code={currency_txt.value}&amount={price_txt.value}&item_name={item_name_txt.value}&return={thanks_url_txt.value}&cancel_return={cancel_url_txt.value}",
            "crypto": lambda: f"{crypto_currency}:{id_txt.value}?amount={amount_txt.value}&message={kwargs.get('msg')}",
        }
    """


    def _build_qr(self):
        """Builds the QR code with the current configurations."""
        self.clear()
        self.add_data(self.data)
        self.make()
        self._apply_styles()

    def _apply_styles(self):
        """Applies the chosen styles and colors to the QR code."""
        # Ensure background color compatibility
        self.back_color = FAKE_BLACK if self.back_color == REAL_BLACK else self.back_color

        # Retrieve selected styles
        color_mask_class = self.color_masks.get(self.colorMask_index)
        body_draw_class = self.shape_drawer.get(self.bodyDrawer_index)
        eye_draw_class = self.shape_drawer.get(self.eyeDrawer_index)
        embed_image = self.logo_path if self.use_logo else None

        # Build the styled image
        if self.use_gradiant and self.colorMask_index != 5:
            self.img = self.make_image(
                image_factory=StyledPilImage,
                module_drawer=body_draw_class,
                eye_drawer=eye_draw_class,
                color_mask=color_mask_class(self.back_color, self.main_color, self.alt_color),
                embeded_image_path=embed_image
            )
        elif self.colorMask_index == 5:
            self.img = self.make_image(
                image_factory=StyledPilImage,
                module_drawer=body_draw_class,
                eye_drawer=eye_draw_class,
                color_mask=ImageColorMask(self.back_color, color_mask_path=self.img_fill_path),
                embeded_image_path=embed_image
            )
        else:
            self.img = self.make_image(
                image_factory=StyledPilImage,
                module_drawer=body_draw_class,
                eye_drawer=eye_draw_class,
                color_mask=SolidFillColorMask(self.back_color, self.main_color),
                embeded_image_path=embed_image
            )

    def generate_preview(self) -> str:
        """Generates a base64-encoded PNG preview of the QR code."""
        self.box_size = 10
        self._build_qr()
        byte_arr = io.BytesIO()
        self.img.save(byte_arr, format='WEBP')
        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")

    def generate_final(self, path: str) -> None:
        """Generates and saves the final QR code image to a specified path."""
        self.box_size = self.real_box_size
        self._build_qr()
        self.img.save(f"{path}.png")

    def get_res(self) -> str:
        """Returns the resolution of the generated QR code."""
        return f"{int(self.img.size[0]/10 * self.real_box_size)} x {int(self.img.size[1]/10 * self.real_box_size)}"