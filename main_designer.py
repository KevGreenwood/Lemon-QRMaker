from flet import *
import flet as ft
from core import *

class QR_Tabs(UserControl):
    def __init__(self):
        super().__init__()
        self.main_txt = TextField(label="Ingrese el contenido")
        self.url_tab = Tab(text="URL")
        self.text_tab = Tab(text="Text")
        self.wifi_tab = Tab(text="WiFi")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.text_tab = Tab(text="Text")
        self.tabs = Tabs(tabs=[self.url_tab, self.text_tab, self.wifi_tab], on_change=self.update, selected_index=0)
        self.cont = Container(padding=10)
        
    def update(self, e):
        title = self.tabs.tabs[self.tabs.selected_index].text
        if title == "URL":
            self.main_txt.value = "https://github.com/KevGreenwood"
            self.main_txt.multiline = False
            self.cont.content = self.main_txt
        if title == "Text":
            self.main_txt.value = ""
            self.main_txt.multiline = True
            self.cont.content = self.main_txt
        #if title == "WiFi":
            
        
        super().update()

    def build(self):
        return Column([self.tabs, self.cont])