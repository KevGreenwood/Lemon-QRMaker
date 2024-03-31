from flet import *
import flet as ft
from core import *
from datetime import date


class App(UserControl):
    def __init__(self):
        super().__init__()

        self.qr = QRGenerator()
        self.data = ""
        self.start_time = ""

        # --- Left Layout ---
        # Text Fields
        self.main_txt = TextField(
            label="Ingrese el contenido",
            value="https://github.com/KevGreenwood",
            on_change=self.regenerate_preview,
        )
        self.filled_txt = TextField(
            label="Ingrese el contenido",
            on_change=self.regenerate_preview,
            multiline=True,
            filled=True,
        )

        self.mail_txt = TextField(
            label="Ingrese su correo electronico", on_change=self.regenerate_preview
        )

        self.phone_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            max_length=16,
            on_change=self.regenerate_preview,
        )

        self.vcard_ver = Dropdown(
            options=
            [
                dropdown.Option("Version 2.1"),
                dropdown.Option("Version 3")
            ]
        )

        self.name_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.lastname_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.org_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.pos_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.work_phone_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            max_length=16,
            on_change=self.regenerate_preview,
        )
        self.priv_phone_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            max_length=16,
            on_change=self.regenerate_preview,
        )
        self.work_fax_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            max_length=12,
            on_change=self.regenerate_preview,
        )
        self.priv_fax_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+]", replacement_string=""
            ),
            max_length=12,
            on_change=self.regenerate_preview,
        )
        self.street_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.zip_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9+-]", replacement_string=""
            ),
            max_length=12,
            on_change=self.regenerate_preview,
        )
        self.city_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.state_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )
        self.country_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )

        self.nickname_txt = TextField(
            label="Ingrese su apellido", on_change=self.regenerate_preview
        )

        self.latitude_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )
        self.longitude_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9-.]", replacement_string=""
            ),
            on_change=self.regenerate_preview,
        )

        self.pass_txt = TextField(
            label="Ingrese el contenido", on_change=self.regenerate_preview
        )

        self.encrypt_drop = Dropdown(
            value="WPA/WPA2",
            options=[
                dropdown.Option("None"),
                dropdown.Option("WEP"),
                dropdown.Option("WPA/WPA2"),
            ],
            on_change=self.regenerate_preview,
        )

        self.location_txt = TextField(
            label="Ingrese el contenido", on_change=self.regenerate_preview
        )

        self.date_picker = DatePicker(on_change=self.regenerate_preview)
        self.time_picker = TimePicker(on_change=self.regenerate_preview)

        self.start_txt = TextField(
            label="Ingrese el contenido",
            on_change=self.regenerate_preview,
            read_only=True,
        )
        self.end_txt = TextField(
            label="Ingrese el contenido",
            on_change=self.regenerate_preview,
            read_only=True,
        )




        self.cypto_drop = Dropdown(
            value="WPA/WPA2",
            options=[
                dropdown.Option("Bitcoin"),
                dropdown.Option("Bitcoin Cash"),
                dropdown.Option("Ethereum"),
                dropdown.Option("Litecoin"),
                dropdown.Option("Dash"),
            ],
            on_change=self.regenerate_preview,
        )
        self.amount_txt = TextField(
            label="Ingrese el contenido",
            input_filter=InputFilter(
                allow=True, regex_string=r"[0-9.]", replacement_string=""
            ),
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
                        src="Assets\\Icons\\whatsapp.svg",
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
                self.event_tab,
                self.app_tab,
                self.fav_tab,
                self.paypal_tab,
                self.bitcoin_tab,
            ],
            on_change=self.update,
            selected_index=0,
        )

        self.cont = Container(self.main_txt, padding=10, width=750)

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
        )
        self.logo = ft.Image(src="default-preview-qr.svg", width=200, height=200)
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
            Column([self.size_panel, self.color_panel, self.logo_panel]), width=750
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
                self.main_txt.value = "https://github.com/KevGreenwood"
                self.cont.content = self.main_txt
                self.back.visible = False

            case 1:
                self.filled_txt.value = ""
                self.cont.content = self.filled_txt

            case 2:
                self.mail_txt.value = ""
                self.main_txt.value = ""
                self.filled_txt.value = ""
                self.cont.content = Column(
                    [self.mail_txt, self.main_txt, self.filled_txt]
                )

            case 3:
                self.phone_txt.value = ""
                self.cont.content = self.phone_txt

            case 4 | 5:
                self.phone_txt.value = ""
                self.filled_txt.value = ""
                self.cont.content = Column([self.phone_txt, self.filled_txt])
                self.forward.visible = True

            case 6:
                self.cont.content = Column(
                    [
                        self.vcard_ver,
                        Row([self.name_txt, self.lastname_txt], spacing=130),
                        Row([self.org_txt, self.pos_txt]),
                        Row([self.work_phone_txt, self.priv_phone_txt]),
                        Row([self.phone_txt, self.work_fax_txt]),
                        Row([self.priv_fax_txt, self.mail_txt]),
                        Row([self.main_txt, self.street_txt]),
                        Row([self.zip_txt, self.city_txt]),
                        Row([self.state_txt, self.country_txt])
                    ]
                )

            case 7:
                self.cont.content = Column(
                    [
                        Row([self.name_txt, self.lastname_txt], spacing=130),
                        Row([self.nickname_txt, self.work_phone_txt]),
                        Row([self.priv_phone_txt, self.phone_txt]),
                        Row([self.mail_txt, self.main_txt]),
                        Row([self.street_txt]),
                        Row([self.zip_txt, self.city_txt]),
                        Row([self.state_txt, self.country_txt]),
                        self.filled_txt
                    ]
                )

            case 8:
                self.latitude_txt.value = ""
                self.longitude_txt.value = ""
                self.cont.content = Column([self.latitude_txt, self.longitude_txt])

            case 9:
                self.main_txt.value = ""
                self.pass_txt.value = ""
                self.encrypt_drop.value = "WPA/WPA2"
                self.cont.content = Column(
                    [self.main_txt, self.pass_txt, self.encrypt_drop]
                )

            case 10:
                self.main_txt.value = ""
                self.location_txt.value = ""
                self.start_txt.value = self.end_txt.value = date.today()
                start_cont = Container(
                    self.start_txt,
                    on_click=lambda _: self.pick_time_date("start"),
                    bgcolor=colors.AMBER,
                )
                end_cont = Container(
                    self.end_txt, on_click=lambda _: self.pick_time_date()
                )

                self.cont.content = Column(
                    [self.main_txt, self.location_txt, start_cont, end_cont]
                )

            case 11:
                self.main_txt.value = ""
                self.cont.content = Column([self.main_txt])

            case 12:
                self.cont.content = Column([self.name_txt, self.main_txt])

            case 14:
                self.forward.visible = False
                self.cont.content = Column([
                    self.cypto_drop,
                    self.main_txt,
                    self.amount_txt,
                    self.nickname_txt,
                    self.filled_txt
                ])

            case _:
                self.forward.visible = True

        if self.tabs.selected_index > 0:
            self.back.visible = True

        super().update()

    # --- QR Building ---
    def build_qr(self):
        wifi_encrypt = ""

        match self.tabs.selected_index:
            case 6:
                pass

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
                print(wifi_encrypt)
            
            case 10:
                pass

        qr_data_formats = {
            0: (self.main_txt.value if self.tabs.selected_index <= 1 else None),
            2: f"mailto:{self.mail_txt.value}?subject={self.filled_txt.value}&body={self.main_txt.value}",
            3: f"tel:{self.phone_txt.value}",
            4: f"SMSTO:{self.phone_txt.value}:{self.filled_txt.value}",
            5: f"https://wa.me/{self.phone_txt.value}/?text={self.filled_txt.value}",
            6: "",
            7: "MECARD:N:{},{};NICKNAME:{};TEL:{};TEL:{};TEL:{};EMAIL:{};BDAY:{};NOTE:{};ADR:,,{},{},{},{},{};;",
            8: f"https://maps.google.com/local?q={self.latitude_txt.value},{self.longitude_txt.value}",
            9: f"WIFI:S:{self.main_txt.value};T:{wifi_encrypt};P:{self.pass_txt.value};;",
            10: f"BEGIN:VEVENT\nUID:{self.main_txt.value}\nORGANIZER:\nSUMMARY:\nLOCATION:\nDTSTART:\nDTEND:\nEND:VEVENT",
            11: f"market://details?id={self.main_txt.value}",
            12: "MEBKM:TITLE:{};URL:{self.main_txt.value};;",
            13: "https://www.paypal.com/cgi-bin/webscr?business={}&cmd=_xclick&currency_code={}&amount={}&item_name={}&return={}&cancel_return={}",
            14: "{}:{}?amount={}&message={}",
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

        print(f"Version: {self.qr.version}\nSize: {self.qr.version}")

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
        self.qr.logo_path = None
        self.qr.use_logo = False
        self.logo.update()
        self.regenerate_preview(e)

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

    def pick_time_date(self, state):
        self.date_picker.pick_date()
        if state == "start":
            self.start_txt.value = f"{self.date_picker.value}"

            self.start_txt.update()

            pure_date = f"{self.date_picker.value}T"
            self.start_time = (
                pure_date.replace(" ", "").replace("-", "").replace(":", "")
            )

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
