from flet import *
import flet as ft
from core import *

class QR_Tabs(UserControl):
    def __init__(self):
        super().__init__()
        
        self.main_txt = TextField(label="Ingrese el contenido") # Use for generic porpouses
        self.alt_txt = TextField(label="Ingrese el contenido")
        self.mail_txt = TextField(label="Ingrese su correo electronico")
        self.phone_txt = TextField(label="Ingrese el contenido", input_filter=NumbersOnlyInputFilter())
        
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

        self.back = IconButton(icon=icons.ARROW_BACK_IOS, on_click=self.go_back)

        self.forward = IconButton(icon=icons.ARROW_FORWARD_IOS, on_click=self.go_forward)

        self.tab_container = Container(Row([self.back, self.tabs, self.forward]))

    def debug(self, e):
        print(self.tabs.selected_index)
    
    def go_back(self, e):
        if self.tabs.selected_index > 0:
            self.tabs.selected_index -= 1
            self.update(e)
        
    def go_forward(self, e):
        if self.tabs.selected_index < 12:
            self.tabs.selected_index += 1
            self.update(e)
    
    def update(self, e):
        if self.tabs.selected_index == 0:
            self.main_txt.value = "https://github.com/KevGreenwood"
            self.main_txt.multiline = False
            self.main_txt.filled = False
            self.cont.content = self.main_txt
        
        if self.tabs.selected_index == 1:
            self.main_txt.value = ""
            self.main_txt.multiline = True
            self.main_txt.filled = True
            self.cont.content = self.main_txt
        
        if self.tabs.selected_index == 2:
            self.mail_txt.value = ""
            self.alt_txt.value = ""
            self.main_txt.value = ""
            self.main_txt.filled = True
            self.cont.content = Column([self.mail_txt, self.alt_txt, self.main_txt])

        if self.tabs.selected_index == 3:
            self.phone_txt.value = ""
            self.cont.content = self.phone_txt

        if self.tabs.selected_index == 4 or self.tabs.selected_index == 5:
            self.phone_txt.value = ""
            self.main_txt.value = ""
            self.main_txt.filled = True
            self.cont.content = Column([self.phone_txt, self.main_txt])

        if self.tabs.selected_index == 6:
                
            self.cont.content = Column([self.main_txt, self.alt_txt, ])
            
        
        super().update()

    def build(self):
        return Column([self.tab_container, self.cont])