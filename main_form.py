from flet import *
import flet as ft
from core import *
from datetime import date


class App(UserControl):
    def __init__(self):
        super().__init__()

        self.qr = QRGenerator()
        self.data: str = ""
        self.start_time: str = ""

        # --- Left Layout ---
        # Text Fields
        # 1
        self.url_txt = TextField(
            label="Website URL",
            value="https://github.com/KevGreenwood",
            hint_text="https://",
            on_change=self.regenerate_preview,
        )
        # 2nd Tab
        self.filled_txt = TextField(
            label="Write your text here",
            on_change=self.regenerate_preview,
            multiline=True,
            filled=True
        )

        self.mail_txt = TextField(
            label="Email Address",
            hint_text="example@email.com",
            on_change=self.regenerate_preview,
        )
        self.subject_txt = TextField(label="Subject", on_change=self.regenerate_preview)
        self.msg_txt = TextField(
            label="Message",
            on_change=self.regenerate_preview,
            multiline=True,
            filled=True
        )

        self.phone_txt = TextField(
            label="Phone Number",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            on_change=self.regenerate_preview
        )

        self.vcard_ver = Dropdown(
            "Version 3",
            label="VCard Version",
            options=[dropdown.Option("Version 2.1"), dropdown.Option("Version 3")],
            on_change=self.regenerate_preview,
        )

        self.name_txt = TextField(
            label="First name", width=360, on_change=self.regenerate_preview
        )
        self.lastname_txt = TextField(
            label="Last name", width=360, on_change=self.regenerate_preview
        )
        self.org_txt = TextField(
            label="Organization", width=360, on_change=self.regenerate_preview
        )
        self.pos_txt = TextField(
            label="Position (Work)", width=360, on_change=self.regenerate_preview
        )
        self.work_phone_txt = TextField(
            label="Phone (Work)",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.priv_phone_txt = TextField(
            label="Phone (Private)",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.work_fax_txt = TextField(
            label="Fax (Work)",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.priv_fax_txt = TextField(
            label="Fax (Private)",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.street_txt = TextField(
            label="Street", width=360, on_change=self.regenerate_preview, multiline=True
        )
        self.zip_txt = TextField(
            label="Zip code",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+-]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.city_txt = TextField(
            label="City", width=360, on_change=self.regenerate_preview
        )
        self.state_txt = TextField(
            label="State", width=360, on_change=self.regenerate_preview
        )
        self.country_txt = TextField(
            label="Country", width=360, on_change=self.regenerate_preview
        )

        self.nickname_txt = TextField(
            label="Nickname", width=360, on_change=self.regenerate_preview
        )

        self.latitude_txt = TextField(
            label="Latitude",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.longitude_txt = TextField(
            label="Longitude",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )

        self.ssid_txt = TextField(
            label="Network Name", hint_text="SSID", on_change=self.regenerate_preview
        )
        self.pass_txt = TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            on_change=self.regenerate_preview,
        )
        self.encrypt_drop = Dropdown(
            "WPA/WPA2",
            label="Network type",
            options=[
                dropdown.Option("None"),
                dropdown.Option("WEP"),
                dropdown.Option("WPA/WPA2"),
            ],
            width=575,
            on_change=self.regenerate_preview,
        )
        self.hidden = Checkbox(
            "Hidden Network", value=False, on_change=self.regenerate_preview
        )

        self.title_txt = TextField(label="Title", on_change=self.regenerate_preview)
        self.location_txt = TextField(
            label="Event Location", on_change=self.regenerate_preview
        )

        # ----- REWORK NEEDED -----
        self.date_picker = DatePicker(on_change=self.regenerate_preview)
        self.time_picker = TimePicker(on_change=self.regenerate_preview)

        self.start_date = TextField(
            label="Event Start Date",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        self.start_time = TextField(
            label="Event Start Time",
            on_change=self.regenerate_preview,
            read_only=True,
        )

        self.end_date = TextField(
            label="Event End Date",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        self.end_time = TextField(
            label="Event End Time",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        # ------------------------------------

        self.app_txt = TextField(
            label="App package name",
            hint_text="Example: com.google.android.youtube",
            helper_text="Search the Internet or use an app to find the package name.",
            on_change=self.regenerate_preview,
        )

        self.cypto_drop = Dropdown(
            "Bitcoin",
            label="Select Cryptocurrency",
            options=[
                dropdown.Option("Bitcoin"),
                dropdown.Option("Bitcoin Cash"),
                dropdown.Option("Ethereum"),
                dropdown.Option("Litecoin"),
                dropdown.Option("Dash"),
            ],
            on_change=self.regenerate_preview,
        )
        self.crypto_adress_txt = TextField(
            label="Receiver",
            hint_text="Bitcoin Address",
            on_change=self.regenerate_preview,
        )
        self.amount_txt = TextField(
            label="Amount",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )
        self.id_txt = TextField(label="ID", on_change=self.regenerate_preview)

        self.payment_drop = Dropdown(
            label="Payment type",
            options=[
                dropdown.Option("Buy now"),
                dropdown.Option("Add to cart"),
                dropdown.Option("Donations"),
            ],
            width=360,
            on_change=self.regenerate_preview,
        )
        self.item_name_txt = TextField(
            label="Item name", width=360, on_change=self.regenerate_preview
        )
        self.item_id_txt = TextField(
            label="Item ID", width=360, on_change=self.regenerate_preview
        )
        self.price_txt = TextField(
            label="Price",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )
        self.currency_txt = TextField(
            label="Currency",
            input_filter=InputFilter(
                allow=True, regex_string=r"[a,...,z]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.ship_txt = TextField(
            label="Shipping",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.tax_txt = TextField(
            label="Tax rate",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )

        # Tabs
        self.url_tab = Tab(
            tab_content=Column(
                [Icon(icons.LINK), Text("URL")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.text_tab = Tab(
            tab_content=Column(
                [Icon(icons.TEXT_SNIPPET), Text("Text")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.mail_tab = Tab(
            tab_content=Column(
                [Icon(icons.MAIL), Text("Email")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.phone_tab = Tab(
            tab_content=Column(
                [Icon(icons.PHONE), Text("Phone")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.sms_tab = Tab(
            tab_content=Column(
                [Icon(icons.SMS), Text("SMS")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.wa_tab = Tab(
            tab_content=Column(
                [
                    ft.Image(
                        src="assets\\icons\\whatsapp.svg",
                        width=24,
                        height=24,
                        color=colors.WHITE,
                    ),
                    Text("Whatsapp"),
                ],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.vcard_tab = Tab(
            tab_content=Column(
                [Icon(icons.PERSON), Text("VCard")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.mcard_tab = Tab(
            tab_content=Column(
                [Icon(icons.PERSON), Text("MeCard")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.location_tab = Tab(
            tab_content=Column(
                [Icon(icons.LOCATION_ON), Text("Location")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.wifi_tab = Tab(
            tab_content=Column(
                [Icon(icons.WIFI), Text("WiFi")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.event_tab = Tab(
            tab_content=Column(
                [Icon(icons.EVENT), Text("Event")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.app_tab = Tab(
            tab_content=Column(
                [Icon(icons.APPS), Text("App")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.fav_tab = Tab(
            tab_content=Column(
                [Icon(icons.BOOKMARK), Text("Favorite")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.paypal_tab = Tab(
            tab_content=Column(
                [Icon(icons.PAYPAL), Text("PayPal")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.bitcoin_tab = Tab(
            tab_content=Column(
                [Icon(icons.CURRENCY_BITCOIN), Text("Bitcoin")],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )

        self.tabs = Tabs(
            tabs=[
                self.url_tab,
                self.text_tab,
                self.mail_tab,
                self.phone_tab,
                self.sms_tab,
                self.wa_tab,
                self.vcard_tab,
                self.mcard_tab,
                self.location_tab,
                self.wifi_tab,
                #self.event_tab,
                self.app_tab,
                self.fav_tab,
                self.paypal_tab,
                self.bitcoin_tab,
            ],
            on_change=self.update,
            selected_index=0,
        )

        self.cont = Container(self.url_txt, padding=10, width=750)

        # Custom Tab
        self.back = IconButton(
            icon=icons.ARROW_BACK_IOS,
            on_click=self.go_back,
            icon_color=colors.WHITE,
            visible=False,
        )
        self.forward = IconButton(
            icon=icons.ARROW_FORWARD_IOS,
            on_click=self.go_forward,
            icon_color=colors.WHITE,
        )
        self.tab_row = Row(
            controls=[
                self.back,
                Column(controls=[self.tabs], expand=True),
                self.forward,
            ],
            width=750,
        )
        self.tabs_container = Container(
            Column([self.tab_row, self.cont]), width=770, alignment=alignment.top_left
        )

        # --- Size Section ---
        self.version_slider = Slider(
            min=1,
            max=40,
            divisions=39,
            label="{value}",
            value=1,
            disabled=True,
            on_change=self.regenerate_preview,
        )
        self.ver_auto_box = Checkbox(
            label="Auto", value=True, on_change=self.switch_version
        )
        self.size_row = Row([self.version_slider, self.ver_auto_box])
        self.border_txt = TextField(
            label="Ingrese el tamaño del borde",
            value="4",
            input_filter=NumbersOnlyInputFilter(),
            on_change=self.regenerate_preview,
        )
        self.size_panel = ExpansionPanelList(
            [
                ExpansionPanel(
                    header=ListTile(title=Text("SET SIZE")),
                    content=Column([self.size_row, self.border_txt]),
                )
            ]
        )

        # --- Color Section ---
        self.color_radio_group = RadioGroup(
            content=Row(
                [
                    Radio(label="Single Color"),
                    Radio(label="Color Gradient"),
                    Checkbox(label="Custom Eye Color"),
                ]
            )
        )
        self.fore_color_txt = TextField(
            label="Foreground Color",
            prefix_icon=icons.COLOR_LENS,
            value="#000000",
            on_change=self.regenerate_preview,
        )
        self.back_color_txt = TextField(
            label="Background Color",
            prefix_icon=icons.COLOR_LENS,
            value="#FFFFFF",
            on_change=self.regenerate_preview,
        )
        self.fore_color_row = Row([self.fore_color_txt])
        self.color_column = Column(
            [self.color_radio_group, self.fore_color_row, self.back_color_txt]
        )
        self.color_panel = ExpansionPanelList(
            [
                ExpansionPanel(
                    header=ListTile(title=Text("SET COLORS")), content=self.color_column
                )
            ]
        )

        # --- Logo Section ---
        self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)
        self.open_logo = ElevatedButton(
            "Upload Logo",
            icon=icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_files_dialog.pick_files(
                allow_multiple=False, allowed_extensions=["png", "jpeg"]
            ),
        )
        self.delete_logo = ElevatedButton(
            "Delete Logo",
            icon=icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
            on_click=self.remove_logo,
            disabled=True,
        )
        self.logo = ft.Image(src="Assets/logo.jpg", width=200, height=200)
        self.logo_preview = Container(self.logo)
        self.logo_row = Row(
            [self.open_logo, self.delete_logo], alignment=MainAxisAlignment.CENTER
        )
        self.logo_column = Column(
            [self.logo_preview, self.logo_row],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        self.logo_panel = ExpansionPanelList(
            [
                ExpansionPanel(
                    header=ListTile(title=Text("ADD LOGO IMAGE")),
                    content=self.logo_column,
                )
            ]
        )




        self.design_panel = ExpansionPanelList(
            [
                ExpansionPanel(
                    header=ListTile(title=Text("CUSTOM DESIGN")),
                )
            ]
        )


        self.correction = Dropdown(label="Correction Level",
            value = "Low",
            options=
            [
                dropdown.Option("Low"),
                dropdown.Option("Medium"),
                dropdown.Option("High"),
                dropdown.Option("Very High")
            ]
        )
        self.advcanced_panel = ExpansionPanelList(
            [
                ExpansionPanel(
                    header=ListTile(title=Text("ADVANCED SETTINGS")),
                    content=self.correction
                )
            ]
        )

        # --- Right Layout ---
        self.save_file_dialog = FilePicker(on_result=self.save_file_result)
        self.save_btn = ElevatedButton(
            "Save",
            icon=icons.SAVE,
            on_click=lambda _: self.save_file_dialog.save_file(
                file_type=FilePickerFileType.IMAGE
            ),
        )
        self.qr_size_slider = Slider(
            min=10,
            max=100,
            divisions=9,
            label="{value}",
            value=50,
            on_change=self.update_scale_txt,
        )

        self.qr_preview = ft.Image(src_base64=self.build_qr(), width=300, height=300)
        self.prev_container = Container(
            alignment=alignment.top_center, content=self.qr_preview
        )

        self.scale_txt = Text(value=self.qr.get_res(), weight=FontWeight.BOLD)
        self.size_row = Row(
            [Text("Low Quality"), self.scale_txt, Text("High Quality")],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )
        self.right = Container(
            Column(
                [
                    self.prev_container,
                    self.qr_size_slider,
                    self.size_row,
                    self.save_btn,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor="white",
            width=500,
        )

        self.main = Container(
            Column([self.size_panel, self.color_panel, self.logo_panel, self.design_panel, self.advcanced_panel]), width=750
        )

    # Custom Tabs
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
                self.url_txt.value = "https://github.com/KevGreenwood"
                self.cont.content = self.url_txt
                self.back.visible = False

            case 1:
                self.filled_txt.value = ""
                self.filled_txt.label = "Write your text here"
                self.cont.content = self.filled_txt

            case 2:
                self.mail_txt.value = ""
                self.subject_txt.value = ""
                self.cont.content = Column(
                    [self.mail_txt, self.subject_txt, self.msg_txt]
                )

            case 3:
                self.phone_txt.value = ""
                self.cont.content = self.phone_txt

            case 4 | 5:
                self.phone_txt.value = ""
                self.cont.content = Column([self.phone_txt, self.msg_txt])
                self.forward.visible = True

            case 6:
                self.phone_txt.width = 360
                self.mail_txt.width = 360
                self.url_txt.width = 360
                self.cont.content = Column(
                    [
                        self.vcard_ver,
                        Row([self.name_txt, self.lastname_txt]),
                        Row([self.org_txt, self.pos_txt]),
                        Row([self.work_phone_txt, self.priv_phone_txt]),
                        Row([self.phone_txt, self.work_fax_txt]),
                        Row([self.priv_fax_txt, self.mail_txt]),
                        Row([self.url_txt, self.street_txt]),
                        Row([self.zip_txt, self.city_txt]),
                        Row([self.state_txt, self.country_txt]),
                    ]
                )

            case 7:
                self.cont.content = Column(
                    [
                        Row([self.name_txt, self.lastname_txt]),
                        Row([self.nickname_txt, self.work_phone_txt]),
                        Row([self.priv_phone_txt, self.phone_txt]),
                        Row([self.mail_txt, self.url_txt]),
                        Row([self.street_txt]),
                        Row([self.zip_txt, self.city_txt]),
                        Row([self.state_txt, self.country_txt]),
                        self.filled_txt,
                    ]
                )

            case 8:
                self.latitude_txt.value = ""
                self.longitude_txt.value = ""
                self.cont.content = Row([self.latitude_txt, self.longitude_txt])

            case 9:
                self.encrypt_drop.value = ""
                self.pass_txt.value = ""
                self.encrypt_drop.value = "WPA/WPA2"
                self.cont.content = Column(
                    [
                        self.ssid_txt,
                        self.pass_txt,
                        Row([self.encrypt_drop, self.hidden]),
                    ]
                )
            
            
            case 15:
                self.url_txt.value = ""
                self.location_txt.value = ""
                #self.start_date.value = self.end_txt.value = date.today()
                self.start_date_cont = Container(
                    self.start_date,
                    on_click=lambda _: self.set_start_date()
                )
                start_time_cont = Container(
                    self.start_time,
                    on_click=lambda _: self.time_picker.pick_time()
                )
                
                end_date_cont = Container(
                    self.end_date, on_click=lambda _: self.pick_time_date()
                )

                self.cont.content = Column(
                    [self.title_txt, self.location_txt, Row([self.start_date_cont, start_time_cont]), end_date_cont]
                )
            

            case 11:
                self.url_txt.value = ""
                self.cont.content = Column([self.app_txt])

            case 12:
                self.cont.content = Column([self.title_txt, self.url_txt])

            case 13:
                self.cont.content = Column(
                    [
                        Row([self.payment_drop, self.mail_txt]),
                        Row([self.item_name_txt, self.item_id_txt]),
                        Row([self.price_txt, self.currency_txt]),
                        Row([self.ship_txt, self.tax_txt]),
                    ]
                )

            case 14:
                self.forward.visible = False
                self.cont.content = Column(
                    [
                        self.cypto_drop,
                        self.crypto_adress_txt,
                        self.amount_txt,
                        self.id_txt,
                        self.msg_txt,
                    ]
                )

            case _:
                self.forward.visible = True

        if self.tabs.selected_index > 0:
            self.back.visible = True

        super().update()

    # --- QR Building ---
    def build_qr(self) -> str:
        wifi_encrypt: str = ""
        network_hide: str = ""
        vcard_v3_txt: str = ""
        crypto_currency: str = ""

        match self.tabs.selected_index:
            case 6:
                if self.vcard_ver.value == "Version 3":
                    vcard_v3_txt = f"BEGIN:VCARD\nVERSION:3.0\nN:{self.lastname_txt.value};{self.name_txt.value}\nFN:{self.name_txt.value} {self.lastname_txt.value}\nTITLE:{self.pos_txt.value}\nORG:{self.org_txt.value}\nURL:{self.url_txt.value}\nEMAIL;TYPE=INTERNET:{self.mail_txt.value}\nTEL;TYPE=voice,work,pref:{self.work_phone_txt.value}\nTEL;TYPE=voice,home,pref:{self.priv_phone_txt.value}\nTEL;TYPE=voice,cell,pref:{self.phone_txt.value}\nTEL;TYPE=fax,work,pref:{self.work_fax_txt.value}\nTEL;TYPE=fax,home,pref:{self.priv_fax_txt.value}\nADR:;;{self.street_txt.value};{self.city_txt.value};{self.state_txt.value};{self.zip_txt.value};{self.country_txt.value}\nEND:VCARD"
                else:
                    vcard_v3_txt = f"BEGIN:VCARD\nVERSION:2.1\nN:{self.lastname_txt.value};{self.name_txt.value}\nTITLE:{self.pos_txt.value}\nORG:{self.org_txt.value}\nURL:{self.url_txt.value}\nEMAIL;TYPE=INTERNET:{self.mail_txt.value}\nTEL;WORK;VOICE:{self.work_phone_txt.value}\nTEL;HOME;VOICE:{self.priv_phone_txt.value}\nTEL;CELL:{self.phone_txt.value}\nTEL;WORK;FAX:{self.work_fax_txt.value}\nTEL;HOME;FAX:{self.priv_fax_txt.value}\nADR:;;{self.street_txt.value};{self.city_txt.value};{self.state_txt.value};{self.zip_txt.value};{self.country_txt.value}\nEND:VCARD"

            case 8:
                if float(self.latitude_txt.value) > 90:
                    self.latitude_txt.value = 90
                if float(self.latitude_txt.value) < -90:
                    self.latitude_txt.value = -90
                self.latitude_txt.update()

                if float(self.longitude_txt.value) > 180:
                    self.longitude_txt.value = 180
                if float(self.longitude_txt.value) < -180:
                    self.longitude_txt.value = -180
                self.longitude_txt.update()

            case 9:
                wifi_encrypt_map = {"None": "nopass", "WEP": "WEP", "WPA/WPA2": "WPA"}
                wifi_encrypt = wifi_encrypt_map.get(self.encrypt_drop.value, None)
                if self.hidden.value:
                    network_hide = "true"
                else:
                    network_hide = "false"

            case 10:
                pass

            case 14:
                crypto_currencies = {
                    "Bitcoin": "bitcoin",
                    "Bitcoin Cash": "bitcoincash",
                    "Ethereum": "ethereum",
                    "Litecoin": "litecoin",
                    "Dash": "dash",
                }
                crypto_currency = crypto_currencies.get(self.cypto_drop.value, None)
        
        qr_data_formats = {
            0: self.url_txt.value,
            1: self.filled_txt.value,
            2: f"mailto:{self.mail_txt.value}?subject={self.subject_txt.value}&body={self.msg_txt.value}",
            3: f"tel:{self.phone_txt.value}",
            4: f"SMSTO:{self.phone_txt.value}:{self.msg_txt.value}",
            5: f"https://wa.me/{self.phone_txt.value}/?text={self.msg_txt.value}",
            6: vcard_v3_txt,
            7: f"MECARD:N:{self.lastname_txt.value},{self.name_txt.value};NICKNAME:{self.nickname_txt.value};TEL:{self.work_phone_txt.value};TEL:{self.priv_phone_txt.value};TEL:{self.phone_txt.value};EMAIL:{self.mail_txt.value};BDAY:;NOTE:{self.filled_txt.value};ADR:,,{self.street_txt.value},{self.city_txt.value},{self.state_txt.value},{self.zip_txt.value},{self.country_txt.value};;",
            8: f"https://maps.google.com/local?q={self.latitude_txt.value},{self.longitude_txt.value}",
            9: f"WIFI:S:{self.ssid_txt.value};T:{wifi_encrypt};P:{self.pass_txt.value};H:{network_hide};;",
            10: f"BEGIN:VEVENT\nUID:{self.url_txt.value}\nORGANIZER:\nSUMMARY:\nLOCATION:\nDTSTART:\nDTEND:\nEND:VEVENT",
            11: f"market://details?id={self.url_txt.value}",
            12: f"MEBKM:TITLE:{self.title_txt};URL:{self.url_txt.value};;",
            13: "https://www.paypal.com/cgi-bin/webscr?business={}&cmd=_xclick&currency_code={}&amount={}&item_name={}&return={}&cancel_return={}",
            14: f"{crypto_currency}:{self.id_txt.value}?amount={self.amount_txt.value}&message={self.msg_txt.value}",
        }
        self.qr.data = qr_data_formats.get(self.tabs.selected_index, None)

        if self.ver_auto_box.value:
            self.qr.version = None
        else:
            self.qr.version = int(self.version_slider.value)

        self.qr.box_size = int(self.qr_size_slider.value)

        if self.border_txt.value == "":
            self.qr.border = 4
        else:
            self.qr.border = int(self.border_txt.value)

        self.qr.back_color = self.back_color_txt.value
        self.qr.main_color = self.fore_color_txt.value

        print(f"Version: {self.qr.version}\nSize: {self.qr.box_size}")

        return self.qr.generate_preview()

    # --- Realtime Building ---
    def regenerate_preview(self, e):
        self.qr_preview.src_base64 = self.build_qr()
        self.qr_preview.update()

    def switch_version(self, e):
        if self.ver_auto_box.value:
            self.version_slider.disabled = True
            self.version_slider.value = 1
        else:
            self.version_slider.disabled = False
        self.version_slider.update()
        self.regenerate_preview(e)

    def remove_logo(self, e):
        if not self.delete_logo.disabled:
            self.qr.logo_path = None
            self.qr.use_logo = False
            self.logo.src = "assets/logo.jpg"
            self.logo.update()
            self.regenerate_preview(e)
            self.delete_logo.disabled = True
            self.delete_logo.update()

    def update_scale_txt(self, e):
        self.regenerate_preview(e)
        self.scale_txt.value = self.qr.get_res()
        self.scale_txt.update()

    def pick_files_result(self, e: FilePickerResultEvent):
        if e.files:  # Prevents Error if you cancel
            for file in e.files:
                print("Nombre del archivo:", file.name)
                print("Ruta del archivo:", file.path)
                print("Tamaño del archivo:", file.size)
            self.logo.src = e.files[0].path
            self.qr.logo_path = e.files[0].path
            self.qr.use_logo = True
            self.logo.update()
            self.regenerate_preview(e)
            self.delete_logo.disabled = False
            self.delete_logo.update()

    def save_file_result(self, e: FilePickerResultEvent):
        if e.path:  # Prevents save a filename named "None" in the app path
            self.qr.generate_final(e.path)

            print(f"Image saved in {e.path}")

            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Image saved in {e.path}"),
                open=True,
                bgcolor=colors.GREEN,
            )
            self.page.update()

    def set_start_date(self):
        self.date_picker.pick_date()
        self.start_date.value = self.date_picker.value
        self.page.update()

    def build(self):
        return Row(
            [
                Column(
                    [self.tabs_container, self.main],
                    height=650,
                    scroll=ScrollMode.ADAPTIVE,
                ),
                self.right,
            ],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.START,
        )

    def did_mount(self):
        self.page.overlay.append(Column([self.date_picker, self.time_picker]))
        self.page.overlay.extend([self.save_file_dialog, self.pick_files_dialog])
        self.page.update()