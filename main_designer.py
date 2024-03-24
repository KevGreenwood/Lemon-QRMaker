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
        self.save_btn = ElevatedButton("Save", icons.SAVE)
        self.qr_size_slider = Slider(min=10, max=100, divisions=9, label="{value}", value=50)
        self.size_row = Row([Text("Low Quality"), Text("666x666 px"), Text("High Quality")], alignment=MainAxisAlignment.SPACE_BETWEEN)

    def build(self):
        return Container(Column([self.prev_container, self.qr_size_slider, self.size_row, self.save_btn], horizontal_alignment=CrossAxisAlignment.CENTER), bgcolor="white", width=500, col=6)

class LeftLayout(UserControl):
    def __init__(self):
        super().__init__()
        # --- Input Section ---
        self.version_slider = Slider(min=1, max=40, divisions=39, label="{value}", value=1, disabled = True)
        self.ver_auto_box = Checkbox(label="Auto", value=True)
        self.size_row = Row([self.version_slider, self.ver_auto_box])
        self.border_txt = TextField(label="Ingrese el tamaño del borde", value="4", input_filter=NumbersOnlyInputFilter())
        self.size_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET SIZE")), content=Column([self.size_row, self.border_txt]))])

        # --- Color Section ---
        self.color_radio_group = RadioGroup(content=Row([
            Radio(label="Single Color"),
            Radio(label="Color Gradient"),
            Checkbox(label="Custom Eye Color")
        ]))
        self.fore_color_txt = TextField(label="Foreground Color", prefix_icon=icons.COLOR_LENS, value="#000000", )
        self.back_color_txt = TextField(label="Background Color", prefix_icon=icons.COLOR_LENS, value="#FFFFFF", )
        self.fore_color_row = Row([self.fore_color_txt])
        self.color_column = Column([self.color_radio_group, self.fore_color_row, self.back_color_txt])
        self.color_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET COLORS")), content=self.color_column)])


    def build(self):
        return Container(Column([self.size_panel, self.color_panel]), width=800, alignment=alignment.top_left)