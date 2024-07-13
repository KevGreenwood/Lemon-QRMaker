from utils.qr_core import *
from widgets.common.TextField import *
from widgets.common.Tab import *
from datetime import date


class App(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.qr = QRGenerator()
        self.data: str = None
        self.start_time: str = None

        # --- Left Layout ---
        url_txt.on_change = self.regenerate_preview
        
        self.hidden = ft.Checkbox(
            "Hidden Network", value=False, on_change=self.regenerate_preview
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

        self.cont = ft.Container(url_txt, padding=10, width=750)
        self.tabs_widget_container = ft.Container(
            ft.Column([tab_row, self.cont]), width=770, alignment=ft.alignment.top_left
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
        
        tabs_widget.on_change = self.update
        back.on_click = self.go_back
        forward.on_click = self.go_forward
    
    # Custom ft.Tabs
    def go_back(self, e):
        if tabs_widget.selected_index > 0:
            tabs_widget.selected_index -= 1
            #back.icon_color = ft.colors.ON_BACKGROUND
        self.update(e)

    def go_forward(self, e):
        if tabs_widget.selected_index < 12:
            tabs_widget.selected_index += 1
            forward.icon_color = ft.colors.ON_BACKGROUND
        self.update(e)

    def update(self, e):
        match tabs_widget.selected_index:
            case 0:
                url_txt.value = "https://github.com/KevGreenwood"
                self.cont.content = url_txt
                back.visible = False

            case 1:
                filled_txt.value = ""
                filled_txt.label = "Write your text here"
                self.cont.content = filled_txt

            case 2:
                mail_txt.value = ""
                subject_txt.value = ""
                self.cont.content = ft.Column(
                    [mail_txt, subject_txt, msg_txt]
                )

            case 3:
                phone_txt.value = ""
                self.cont.content = phone_txt

            case 4:
                phone_txt.value = ""
                self.cont.content = ft.Column([phone_txt, msg_txt])
                forward.visible = True
                
            case 5:
                whatsapp_icon.color = ft.colors.PRIMARY
                phone_txt.value = ""
                self.cont.content = ft.Column([phone_txt, msg_txt])
                forward.visible = True

            case 6:
                phone_txt.width = 360
                mail_txt.width = 360
                url_txt.width = 360
                self.cont.content = ft.Column(
                    [
                        self.vcard_ver,
                        ft.Row([name_txt, lastname_txt]),
                        ft.Row([org_txt, pos_txt]),
                        ft.Row([work_phone_txt, priv_phone_txt]),
                        ft.Row([phone_txt, work_fax_txt]),
                        ft.Row([priv_fax_txt, mail_txt]),
                        ft.Row([url_txt, street_txt]),
                        ft.Row([zip_txt, city_txt]),
                        ft.Row([state_txt, country_txt]),
                    ]
                )

            case 7:
                self.cont.content = ft.Column(
                    [
                        ft.Row([name_txt, lastname_txt]),
                        ft.Row([nickname_txt, work_phone_txt]),
                        ft.Row([priv_phone_txt, phone_txt]),
                        ft.Row([mail_txt, url_txt]),
                        ft.Row([street_txt]),
                        ft.Row([zip_txt, city_txt]),
                        ft.Row([state_txt, country_txt]),
                        filled_txt,
                    ]
                )

            case 8:
                latitude_txt.value = ""
                longitude_txt.value = ""
                self.cont.content = ft.Row([latitude_txt, longitude_txt])

            case 9:
                self.encrypt_drop.value = ""
                pass_txt.value = ""
                self.encrypt_drop.value = "WPA/WPA2"
                self.cont.content = ft.Column(
                    [
                        ssid_txt,
                        pass_txt,
                        ft.Row([self.encrypt_drop, self.hidden]),
                    ]
                )
                        
            case 15:
                url_txt.value = ""
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
                self.cont.content = ft.Column([app_txt])

            case 12:
                self.cont.content = ft.Column([title_txt, url_txt])

            case 13:
                self.cont.content = ft.Column(
                    [
                        ft.Row([self.payment_drop, mail_txt]),
                        ft.Row([item_name_txt, item_id_txt]),
                        ft.Row([price_txt, currency_txt]),
                        ft.Row([ship_txt, tax_txt]),
                    ]
                )

            case 14:
                forward.visible = False
                self.cont.content = ft.Column(
                    [
                        self.cypto_drop,
                        crypto_address_txt,
                        amount_txt,
                        id_txt,
                        msg_txt,
                    ]
                )

            case _:
                forward.visible = True

        if tabs_widget.selected_index != 5:
            whatsapp_icon.color = ft.colors.ON_BACKGROUND
        
        if tabs_widget.selected_index > 0:
            back.visible = True

        super().update()

    # --- QR Building ---
    def build_qr(self) -> str:
        wifi_encrypt: str = ""
        network_hide: str = ""
        vcard_v3_txt: str = ""
        crypto_currency: str = ""

        match tabs_widget.selected_index:
            case 6:
                if self.vcard_ver.value == "Version 3":
                    vcard_v3_txt = f"BEGIN:VCARD\nVERSION:3.0\nN:{lastname_txt.value};{name_txt.value}\nFN:{name_txt.value} {lastname_txt.value}\nTITLE:{pos_txt.value}\nORG:{org_txt.value}\nURL:{url_txt.value}\nEMAIL;TYPE=INTERNET:{mail_txt.value}\nTEL;TYPE=voice,work,pref:{work_phone_txt.value}\nTEL;TYPE=voice,home,pref:{priv_phone_txt.value}\nTEL;TYPE=voice,cell,pref:{phone_txt.value}\nTEL;TYPE=fax,work,pref:{work_fax_txt.value}\nTEL;TYPE=fax,home,pref:{priv_fax_txt.value}\nADR:;;{street_txt.value};{city_txt.value};{state_txt.value};{zip_txt.value};{country_txt.value}\nEND:VCARD"
                else:
                    vcard_v3_txt = f"BEGIN:VCARD\nVERSION:2.1\nN:{lastname_txt.value};{name_txt.value}\nTITLE:{pos_txt.value}\nORG:{org_txt.value}\nURL:{url_txt.value}\nEMAIL;TYPE=INTERNET:{mail_txt.value}\nTEL;WORK;VOICE:{work_phone_txt.value}\nTEL;HOME;VOICE:{priv_phone_txt.value}\nTEL;CELL:{phone_txt.value}\nTEL;WORK;FAX:{work_fax_txt.value}\nTEL;HOME;FAX:{priv_fax_txt.value}\nADR:;;{street_txt.value};{city_txt.value};{state_txt.value};{zip_txt.value};{country_txt.value}\nEND:VCARD"

            case 8:
                if float(latitude_txt.value) > 90:
                    latitude_txt.value = 90
                if float(latitude_txt.value) < -90:
                    latitude_txt.value = -90
                latitude_txt.update()

                if float(longitude_txt.value) > 180:
                    longitude_txt.value = 180
                if float(longitude_txt.value) < -180:
                    longitude_txt.value = -180
                longitude_txt.update()

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
            0: url_txt.value,
            1: filled_txt.value,
            2: f"mailto:{mail_txt.value}?subject={subject_txt.value}&body={msg_txt.value}",
            3: f"tel:{phone_txt.value}",
            4: f"SMSTO:{phone_txt.value}:{msg_txt.value}",
            5: f"https://wa.me/{phone_txt.value}/?text={msg_txt.value}",
            6: vcard_v3_txt,
            7: f"MECARD:N:{lastname_txt.value},{name_txt.value};NICKNAME:{nickname_txt.value};TEL:{work_phone_txt.value};TEL:{priv_phone_txt.value};TEL:{phone_txt.value};EMAIL:{mail_txt.value};BDAY:;NOTE:{filled_txt.value};ADR:,,{street_txt.value},{city_txt.value},{state_txt.value},{zip_txt.value},{country_txt.value};;",
            8: f"https://maps.google.com/local?q={latitude_txt.value},{longitude_txt.value}",
            9: f"WIFI:S:{ssid_txt.value};T:{wifi_encrypt};P:{pass_txt.value};H:{network_hide};;",
            10: f"BEGIN:VEVENT\nUID:{url_txt.value}\nORGANIZER:\nSUMMARY:\nLOCATION:\nDTSTART:\nDTEND:\nEND:VEVENT",
            11: f"market://details?id={app_txt.value}",
            12: f"MEBKM:TITLE:{title_txt};URL:{url_txt.value};;",
            13: "https://www.paypal.com/cgi-bin/webscr?business={}&cmd=_xclick&currency_code={}&amount={}&item_name={}&return={}&cancel_return={}",
            14: f"{crypto_currency}:{id_txt.value}?amount={amount_txt.value}&message={msg_txt.value}",
        }
        self.qr.data = qr_data_formats.get(tabs_widget.selected_index, None)

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
                    [self.tabs_widget_container, self.main],
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