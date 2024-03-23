from flet import *
import flet as ft
from core import *

class QR_Tabs(UserControl):
    def __init__(self):
        super().__init__()
        
        self.main_txt = TextField(label="Ingrese el contenido") # Use for generic porpouses
        self.alt_txt = TextField(label="Ingrese el contenido")
        self.mail_txt = TextField(label="Ingrese su correo electronico")
        self.phone_txt = TextField(label="Ingrese el contenido", input_filter=InputFilter(allow=True,
            regex_string=r"[0-9+]",
            replacement_string=""), max_length=16)
        
        self.url_tab = Tab(tab_content=Column([Icon(icons.LINK), Text("URL")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.text_tab = Tab(tab_content=Column([Icon(icons.TEXT_SNIPPET), Text("Text")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.mail_tab = Tab(tab_content=Column([Icon(icons.MAIL), Text("Email")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.phone_tab = Tab(tab_content=Column([Icon(icons.PHONE), Text("Phone")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.sms_tab = Tab(tab_content=Column([Icon(icons.SMS), Text("SMS")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.wa_tab = Tab(tab_content=Column([ft.Image(src="Assets\\Icons\\whatsapp.svg", width=24, height=24, color=colors.WHITE), Text("Whatsapp")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.vcard_tab = Tab(tab_content=Column([Icon(icons.CONTACT_PAGE), Text("VCard")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.mcard_tab = Tab(tab_content=Column([Icon(icons.CONTACT_PAGE), Text("MeCard")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.location_tab = Tab(tab_content=Column([Icon(icons.LOCATION_ON), Text("Location")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.wifi_tab = Tab(tab_content=Column([Icon(icons.WIFI), Text("WiFi")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.event_tab = Tab(tab_content=Column([Icon(icons.EVENT), Text("Event")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.paypal_tab = Tab(tab_content=Column([Icon(icons.PAYPAL), Text("PayPal")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
        self.bitcoin_tab = Tab(tab_content=Column([Icon(icons.CURRENCY_BITCOIN), Text("Bitcoin")], spacing=0, horizontal_alignment=CrossAxisAlignment.CENTER))
    
        self.tabs = Tabs(tabs=
            [
                self.url_tab, self.text_tab, self.mail_tab, self.phone_tab, 
                self.sms_tab, self.wa_tab, self.vcard_tab, self.mcard_tab, 
                self.location_tab, self.wifi_tab, self.event_tab, self.paypal_tab,
                self.bitcoin_tab
            ], on_change=self.update, selected_index=0)
        

        self.cont = Container(padding=10)

        self.back = IconButton(icon=icons.ARROW_BACK_IOS, on_click=self.go_back, icon_color=colors.WHITE, width=30, visible=False)

        self.forward = IconButton(icon=icons.ARROW_FORWARD_IOS, on_click=self.go_forward, icon_color=colors.WHITE, width=30)

        self.tab_row = Row(controls=[self.back, Column(controls=[self.tabs], expand=True), self.forward])
    
    def go_back(self, e):
        if self.tabs.selected_index > 0:
            self.tabs.selected_index -= 1
            self.back.icon_color = colors.WHITE
        self.update(e)
    
    def go_forward(self, e):
        if self.tabs.selected_index < 12:
            self.tabs.selected_index += 1
            self.forward.icon_color = colors.WHITE
        self.update(e)
    
    def update(self, e):
        match self.tabs.selected_index:
            case 0:
                self.main_txt.value = "https://github.com/KevGreenwood"
                self.main_txt.multiline = False
                self.main_txt.filled = False
                self.cont.content = self.main_txt
                self.back.visible = False

            case 1:
                self.main_txt.value = ""
                self.main_txt.multiline = True
                self.main_txt.filled = True
                self.cont.content = self.main_txt
        
            case 2:
                self.mail_txt.value = ""
                self.alt_txt.value = ""
                self.main_txt.value = ""
                self.main_txt.filled = True
                self.cont.content = Column([self.mail_txt, self.alt_txt, self.main_txt])

            case 3:
                self.phone_txt.value = ""
                self.cont.content = self.phone_txt

            case 4 | 5:
                self.phone_txt.value = ""
                self.main_txt.value = ""
                self.main_txt.filled = True
                self.cont.content = Column([self.phone_txt, self.main_txt])
                self.forward.visible = True

            case 6:
                self.cont.content = Column([self.main_txt, self.alt_txt, ])
                
            case 12:
                self.forward.visible = False
            
            case _:
                self.forward.visible = True

        if self.tabs.selected_index > 0:
            self.back.visible = True

        super().update()

    def build(self):
        return Container(Column([self.tab_row, self.cont]), width=800, alignment=alignment.top_left)

class RightLayout(UserControl):
    def __init__(self):
        super().__init__()
        self.qr_preview = ft.Image(src="default-preview-qr.svg",width=300, height=300)
        self.prev_container = Container(alignment=alignment.top_center, content=self.qr_preview)
    def build(self):
        return Container(Column([self.prev_container]), bgcolor="white", width=500, col=6)