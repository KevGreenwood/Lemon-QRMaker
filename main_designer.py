from flet import *
import flet as ft
from core import *

class CustomTab(UserControl):
    def __init__(self, icon, text: str):
        super().__init__()
        self.icon = icon
        self.text = text

    def build(self):
        return Tab(tab_content=Column([Icon(self.icon), Text(self.text)], spacing=0))

class QR_Tabs(UserControl):
    def __init__(self):
        super().__init__()
        self.main_txt = TextField(label="Ingrese el contenido") # Use for generic porpouses
        self.alt_txt = TextField(label="Ingrese el contenido")
        self.mail_txt = TextField(label="Ingrese su correo electronico")

        self.url_tab = CustomTab(icons.LINK, "URL")

        self.phone_txt = TextField(label="Ingrese el contenido", input_filter=NumbersOnlyInputFilter())
        #self.url_tab = Tab(tab_content=Column([Icon(icons.LINK), Text("URL")], spacing=0))
        self.text_tab = Tab(text="Text")
        self.mail_tab = Tab(text="Email")
        self.phone_tab = Tab(text="Phone")
        self.sms_tab = Tab(text="SMS")
        self.wa_tab = Tab(text="Whatsapp")
        self.vcard_tab = Tab(text="VCard")
        self.mcard_tab = Tab(text="MeCard")
        self.location_tab = Tab(text="Location")
        self.wifi_tab = Tab(text="WiFi")
        self.event_tab = Tab(text="Event")
        self.paypal_tab = Tab(text="PayPal")
        self.bitcoin_tab = Tab(text="Bitcoin")

        self.tabs = Tabs(tabs=
            [
                self.url_tab, self.text_tab, self.mail_tab, self.phone_tab, 
                self.sms_tab, self.wa_tab, self.vcard_tab, self.mcard_tab, 
                self.location_tab, self.wifi_tab, self.event_tab, self.paypal_tab,
                self.bitcoin_tab
            ], on_change=self.update, selected_index=0)
        
        self.cont = Container(padding=10)
        
    def update(self, e):
        title = self.tabs.tabs[self.tabs.selected_index].text
        if title == "URL":
            self.main_txt.value = "https://github.com/KevGreenwood"
            self.main_txt.multiline = False
            self.main_txt.filled = False
            self.cont.content = self.main_txt
        
        if title == "Text":
            self.main_txt.value = ""
            self.main_txt.multiline = True
            self.main_txt.filled = True
            self.cont.content = self.main_txt
        
        if title == "Email":
            self.mail_txt.value = ""
            self.alt_txt.value = ""
            self.main_txt.value = ""
            self.main_txt.filled = True
            self.cont.content = Column([self.mail_txt, self.alt_txt, self.main_txt])

        if title == "Phone":
            self.phone_txt.value = ""
            self.cont.content = self.phone_txt

        if title == "SMS" or title == "Whatsapp":
            self.phone_txt.value = ""
            self.main_txt.value = ""
            self.main_txt.filled = True
            self.cont.content = Column([self.phone_txt, self.main_txt])

        if title == "WiFi":
                
            self.cont.content = Column([self.main_txt, self.alt_txt, ])
            
        
        super().update()

    def build(self):
        return Column([self.tabs, self.cont])