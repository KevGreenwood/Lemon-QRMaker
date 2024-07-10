import flet as ft
from core import *
from datetime import date


class App(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.qr = QRGenerator()
        self.data: str = None
        self.start_time: str = None

        # --- Left Layout ---
        # Text Fields
        # 1
        self.url_txt = ft.TextField(
            label="Website URL",
            value="https://github.com/KevGreenwood",
            hint_text="https://",
            on_change=self.regenerate_preview,
        )
        # 2nd ft.Tab
        self.filled_txt = ft.TextField(
            label="Write your text here",
            on_change=self.regenerate_preview,
            multiline=True,
            filled=True
        )

        self.mail_txt = ft.TextField(
            label="Email Address",
            hint_text="example@email.com",
            on_change=self.regenerate_preview,
        )
        self.subject_txt = ft.TextField(label="Subject", on_change=self.regenerate_preview)
        self.msg_txt = ft.TextField(
            label="Message",
            on_change=self.regenerate_preview,
            multiline=True,
            filled=True
        )

        self.phone_txt = ft.TextField(
            label="Phone Number",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            on_change=self.regenerate_preview
        )

        self.vcard_ver = ft.Dropdown(
            "Version 3",
            label="VCard Version",
            options=[ft.dropdown.Option("Version 2.1"), ft.dropdown.Option("Version 3")],
            on_change=self.regenerate_preview,
        )

        self.name_txt = ft.TextField(
            label="First name", width=360, on_change=self.regenerate_preview
        )
        self.lastname_txt = ft.TextField(
            label="Last name", width=360, on_change=self.regenerate_preview
        )
        self.org_txt = ft.TextField(
            label="Organization", width=360, on_change=self.regenerate_preview
        )
        self.pos_txt = ft.TextField(
            label="Position (Work)", width=360, on_change=self.regenerate_preview
        )
        self.work_phone_txt = ft.TextField(
            label="Phone (Work)",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.priv_phone_txt = ft.TextField(
            label="Phone (Private)",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.work_fax_txt = ft.TextField(
            label="Fax (Work)",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.priv_fax_txt = ft.TextField(
            label="Fax (Private)",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.street_txt = ft.TextField(
            label="Street", width=360, on_change=self.regenerate_preview, multiline=True
        )
        self.zip_txt = ft.TextField(
            label="Zip code",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9+-]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.city_txt = ft.TextField(
            label="City", width=360, on_change=self.regenerate_preview
        )
        self.state_txt = ft.TextField(
            label="State", width=360, on_change=self.regenerate_preview
        )
        self.country_txt = ft.TextField(
            label="Country", width=360, on_change=self.regenerate_preview
        )

        self.nickname_txt = ft.TextField(
            label="Nickname", width=360, on_change=self.regenerate_preview
        )

        self.latitude_txt = ft.TextField(
            label="Latitude",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.longitude_txt = ft.TextField(
            label="Longitude",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )

        self.ssid_txt = ft.TextField(
            label="Network Name", hint_text="SSID", on_change=self.regenerate_preview
        )
        self.pass_txt = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            on_change=self.regenerate_preview,
        )
        self.encrypt_drop = ft.Dropdown(
            "WPA/WPA2",
            label="Network type",
            options=[
                ft.dropdown.Option("None"),
                ft.dropdown.Option("WEP"),
                ft.dropdown.Option("WPA/WPA2"),
            ],
            width=575,
            on_change=self.regenerate_preview,
        )
        self.hidden = ft.Checkbox(
            "Hidden Network", value=False, on_change=self.regenerate_preview
        )

        self.title_txt = ft.TextField(label="Title", on_change=self.regenerate_preview)
        self.location_txt = ft.TextField(
            label="Event Location", on_change=self.regenerate_preview
        )

        # ----- REWORK NEEDED -----
        self.date_picker = ft.DatePicker(on_change=self.regenerate_preview)
        self.time_picker = ft.TimePicker(on_change=self.regenerate_preview)

        self.start_date = ft.TextField(
            label="Event Start Date",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        self.start_time = ft.TextField(
            label="Event Start Time",
            on_change=self.regenerate_preview,
            read_only=True,
        )

        self.end_date = ft.TextField(
            label="Event End Date",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        self.end_time = ft.TextField(
            label="Event End Time",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        # ------------------------------------

        self.app_txt = ft.TextField(
            label="App package name",
            hint_text="Example: com.google.android.youtube",
            helper_text="Search the Internet or use an app to find the package name.",
            on_change=self.regenerate_preview
        )

        self.cypto_drop = ft.Dropdown(
            "Bitcoin",
            label="Select Cryptocurrency",
            options=[
                ft.dropdown.Option("Bitcoin"),
                ft.dropdown.Option("Bitcoin Cash"),
                ft.dropdown.Option("Ethereum"),
                ft.dropdown.Option("Litecoin"),
                ft.dropdown.Option("Dash"),
            ],
            on_change=self.regenerate_preview,
        )
        self.crypto_address_txt = ft.TextField(
            label="Receiver",
            hint_text="Bitcoin Address",
            on_change=self.regenerate_preview,
        )
        self.amount_txt = ft.TextField(
            label="Amount",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )
        self.id_txt = ft.TextField(label="ID", on_change=self.regenerate_preview)

        self.payment_drop = ft.Dropdown(
            label="Payment type",
            options=[
                ft.dropdown.Option("Buy now"),
                ft.dropdown.Option("Add to cart"),
                ft.dropdown.Option("Donations"),
            ],
            width=360,
            on_change=self.regenerate_preview,
        )
        self.item_name_txt = ft.TextField(
            label="Item name", width=360, on_change=self.regenerate_preview
        )
        self.item_id_txt = ft.TextField(
            label="Item ID", width=360, on_change=self.regenerate_preview
        )
        self.price_txt = ft.TextField(
            label="Price",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )
        self.currency_txt = ft.TextField(
            label="Currency",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[a,...,z]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.ship_txt = ft.TextField(
            label="Shipping",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )
        self.tax_txt = ft.TextField(
            label="Tax rate",
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
            width=360,
            on_change=self.regenerate_preview,
        )

        # ft.Tabs
        self.url_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.LINK), ft.Text("URL")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.text_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.TEXT_SNIPPET), ft.Text("Text")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.mail_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.MAIL), ft.Text("Email")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.phone_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PHONE), ft.Text("Phone")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.sms_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.SMS), ft.Text("SMS")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.wa_tab = ft.Tab(
            tab_content=ft.Column(
                [
                    ft.Image(
                        src="assets\\icons\\whatsapp.svg",
                        width=24,
                        height=24,
                        color=ft.colors.WHITE,
                    ),
                    ft.Text("Whatsapp"),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.vcard_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PERSON), ft.Text("VCard")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.mcard_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PERSON), ft.Text("MeCard")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.location_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.LOCATION_ON), ft.Text("Location")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.wifi_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.WIFI), ft.Text("WiFi")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.event_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.EVENT), ft.Text("Event")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.app_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.APPS), ft.Text("App")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.fav_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.BOOKMARK), ft.Text("Favorite")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.paypal_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PAYPAL), ft.Text("PayPal")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.bitcoin_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.CURRENCY_BITCOIN), ft.Text("Bitcoin")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        self.tabs = ft.Tabs(
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
                self.event_tab,
                self.app_tab,
                self.fav_tab,
                self.paypal_tab,
                self.bitcoin_tab,
            ],
            on_change=self.update,
            selected_index=0,
        )

        self.cont = ft.Container(self.url_txt, padding=10, width=750)

        # Custom ft.Tab
        self.back = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=self.go_back,
            icon_color=ft.colors.WHITE,
            visible=False,
        )
        self.forward = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD_IOS,
            on_click=self.go_forward,
            icon_color=ft.colors.WHITE,
        )
        self.tab_row = ft.Row(
            controls=[
                self.back,
                ft.Column(controls=[self.tabs], expand=True),
                self.forward,
            ],
            width=750,
        )
        self.tabs_container = ft.Container(
            ft.Column([self.tab_row, self.cont]), width=770, alignment=ft.alignment.top_left
        )

        # --- Size Section ---
        self.version_slider = ft.Slider(
            min=1,
            max=40,
            divisions=39,
            label="{value}",
            value=1,
            disabled=True,
            on_change=self.regenerate_preview,
        )
        self.ver_auto_box = ft.Checkbox(
            label="Auto", value=True, on_change=self.switch_version
        )
        self.size_row = ft.Row([self.version_slider, self.ver_auto_box])
        self.border_txt = ft.TextField(
            label="Ingrese el tamaño del borde",
            value="4",
            input_filter=ft.NumbersOnlyInputFilter(),
            on_change=self.regenerate_preview,
        )
        
        self.size_panel = ft.ExpansionPanelList(
            [
                ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text("SET SIZE")),
                    content=ft.Container(ft.Column([self.size_row, self.border_txt]), padding=20),
                )
            ]
        )

        # --- Color Section ---
        self.color_radio_group = ft.RadioGroup(
            content=ft.Row(
                [
                    ft.Radio(value="normal", label="Single Color"),
                    ft.Radio(value="gradient", label="Color Gradient")
                ]
            ), value="normal"
        )
        self.custom_eye = ft.Checkbox(label="Custom Eye Color")
        self.fore_color_txt = ft.TextField(
            label="Foreground Color",
            prefix_icon=ft.icons.COLOR_LENS,
            value="#000000",
            on_change=self.regenerate_preview,
        )
        self.back_color_txt = ft.TextField(
            label="Background Color",
            prefix_icon=ft.icons.COLOR_LENS,
            value="#FFFFFF",
            on_change=self.regenerate_preview,
        )
        self.fore_color_row = ft.Row([self.fore_color_txt])
        self.color_column = ft.Column(
            [self.color_radio_group, self.custom_eye, self.fore_color_row, self.back_color_txt]
        )
        
        self.color_panel = ft.ExpansionPanelList(
            [
                ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text("SET COLORS")), content=ft.Container(self.color_column, padding=20))
            ]
        )

        # --- Logo Section ---
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.open_logo = ft.ElevatedButton(
            "Upload Logo",
            icon=ft.icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_files_dialog.pick_files(
                allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "svg", "webp"]
            ),
        )
        self.delete_logo = ft.ElevatedButton(
            "Delete Logo",
            icon=ft.icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
            on_click=self.remove_logo,
            disabled=True,
        )
        self.logo = ft.Image(src="Assets/logo.jpg", width=250, height=250)
        
        self.logo_row = ft.Row(
            [self.open_logo, self.delete_logo], alignment=ft.MainAxisAlignment.CENTER, height=50
        )
        self.logo_column = ft.Column(
            controls=[self.logo, self.logo_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.logo_panel = ft.ExpansionPanelList(
            [
                ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text("ADD LOGO IMAGE")),
                    content=ft.Container(self.logo_column, padding=20),
                )
            ]
        )




        self.design_panel = ft.ExpansionPanelList(
            [
                ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text("CUSTOM DESIGN")),
                )
            ]
        )


        self.correction = ft.Dropdown(label="Correction Level",
            value = "Low",
            options=
            [
                ft.dropdown.Option("Low"),
                ft.dropdown.Option("Medium"),
                ft.dropdown.Option("High"),
                ft.dropdown.Option("Very High")
            ]
        )
        self.advanced_panel = ft.ExpansionPanelList(
            [
                ft.ExpansionPanel(
                    header=ft.ListTile(title=ft.Text("ADVANCED SETTINGS")),
                    content=ft.Container(self.correction, padding=20)
                )
            ]
        )

        # --- Right Layout ---
        self.save_file_dialog = ft.FilePicker(on_result=self.save_file_result)
        self.save_btn = ft.ElevatedButton(
            "Save",
            icon=ft.icons.SAVE,
            on_click=lambda _: self.save_file_dialog.save_file(
                file_type=ft.FilePickerFileType.IMAGE
            ),
        )
        self.qr_size_slider = ft.Slider(
            min=10,
            max=100,
            divisions=9,
            label="{value}",
            value=50,
            on_change=self.update_scale_txt,
        )

        self.qr_preview = ft.Image(src_base64=self.build_qr(), width=400, height=400)
        self.prev_container = ft.Container(
            alignment=ft.alignment.top_center, content=self.qr_preview
        )

        self.scale_txt = ft.Text(value=self.qr.get_res(), weight=ft.FontWeight.BOLD)
        self.size_row = ft.Row(
            [ft.Text("Low Quality"), self.scale_txt, ft.Text("High Quality")],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        self.right = ft.Container(
            ft.Column(
                [
                    self.prev_container,
                    self.qr_size_slider,
                    self.size_row,
                    self.save_btn,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="white",
            width=500,
            height=1500
        )

        self.main = ft.Container(
            ft.Column([self.size_panel, self.color_panel, self.logo_panel, self.design_panel, self.advanced_panel]), width=750
        )

    # Custom ft.Tabs
    def go_back(self, e):
        if self.tabs.selected_index > 0:
            self.tabs.selected_index -= 1
            self.back.icon_color = ft.colors.WHITE
        self.update(e)

    def go_forward(self, e):
        if self.tabs.selected_index < 12:
            self.tabs.selected_index += 1
            self.forward.icon_color = ft.colors.WHITE
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
                self.cont.content = ft.Column(
                    [self.mail_txt, self.subject_txt, self.msg_txt]
                )

            case 3:
                self.phone_txt.value = ""
                self.cont.content = self.phone_txt

            case 4 | 5:
                self.phone_txt.value = ""
                self.cont.content = ft.Column([self.phone_txt, self.msg_txt])
                self.forward.visible = True

            case 6:
                self.phone_txt.width = 360
                self.mail_txt.width = 360
                self.url_txt.width = 360
                self.cont.content = ft.Column(
                    [
                        self.vcard_ver,
                        ft.Row([self.name_txt, self.lastname_txt]),
                        ft.Row([self.org_txt, self.pos_txt]),
                        ft.Row([self.work_phone_txt, self.priv_phone_txt]),
                        ft.Row([self.phone_txt, self.work_fax_txt]),
                        ft.Row([self.priv_fax_txt, self.mail_txt]),
                        ft.Row([self.url_txt, self.street_txt]),
                        ft.Row([self.zip_txt, self.city_txt]),
                        ft.Row([self.state_txt, self.country_txt]),
                    ]
                )

            case 7:
                self.cont.content = ft.Column(
                    [
                        ft.Row([self.name_txt, self.lastname_txt]),
                        ft.Row([self.nickname_txt, self.work_phone_txt]),
                        ft.Row([self.priv_phone_txt, self.phone_txt]),
                        ft.Row([self.mail_txt, self.url_txt]),
                        ft.Row([self.street_txt]),
                        ft.Row([self.zip_txt, self.city_txt]),
                        ft.Row([self.state_txt, self.country_txt]),
                        self.filled_txt,
                    ]
                )

            case 8:
                self.latitude_txt.value = ""
                self.longitude_txt.value = ""
                self.cont.content = ft.Row([self.latitude_txt, self.longitude_txt])

            case 9:
                self.encrypt_drop.value = ""
                self.pass_txt.value = ""
                self.encrypt_drop.value = "WPA/WPA2"
                self.cont.content = ft.Column(
                    [
                        self.ssid_txt,
                        self.pass_txt,
                        ft.Row([self.encrypt_drop, self.hidden]),
                    ]
                )
            
            
            case 15:
                self.url_txt.value = ""
                self.location_txt.value = ""
                #self.start_date.value = self.end_txt.value = date.today()
                self.start_date_cont = ft.Container(
                    self.start_date,
                    on_click=lambda _: self.set_start_date()
                )
                start_time_cont = ft.Container(
                    self.start_time,
                    on_click=lambda _: self.time_picker.pick_time()
                )
                
                end_date_cont = ft.Container(
                    self.end_date, on_click=lambda _: self.pick_time_date()
                )

                self.cont.content = ft.Column(
                    [self.title_txt, self.location_txt, ft.Row([self.start_date_cont, start_time_cont]), end_date_cont]
                )
            

            case 11:
                self.cont.content = ft.Column([self.app_txt])

            case 12:
                self.cont.content = ft.Column([self.title_txt, self.url_txt])

            case 13:
                self.cont.content = ft.Column(
                    [
                        ft.Row([self.payment_drop, self.mail_txt]),
                        ft.Row([self.item_name_txt, self.item_id_txt]),
                        ft.Row([self.price_txt, self.currency_txt]),
                        ft.Row([self.ship_txt, self.tax_txt]),
                    ]
                )

            case 14:
                self.forward.visible = False
                self.cont.content = ft.Column(
                    [
                        self.cypto_drop,
                        self.crypto_address_txt,
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
            11: f"market://details?id={self.app_txt.value}",
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

    def pick_files_result(self, e: ft.FilePickerResultEvent):
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

    def save_file_result(self, e: ft.FilePickerResultEvent):
        if e.path:  # Prevents save a filename named "None" in the app path
            self.qr.generate_final(e.path)

            print(f"Image saved in {e.path}")

            self.page.snack_bar = ft.SnackBar(
                content=ft.ft.Text(f"Image saved in {e.path}"),
                open=True,
                bgcolor=ft.colors.GREEN,
            )
            self.page.update()

    def set_start_date(self):
        self.date_picker.pick_date()
        self.start_date.value = self.date_picker.value
        self.page.update()

    def build(self):
        return ft.Row(
            [
                ft.Column(
                    [self.tabs_container, self.main],
                    height=650,
                    scroll=ft.ScrollMode.ADAPTIVE,
                ),
                self.right,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def did_mount(self):
        self.page.overlay.append(ft.Column([self.date_picker, self.time_picker]))
        self.page.overlay.extend([self.save_file_dialog, self.pick_files_dialog])
        self.page.update()