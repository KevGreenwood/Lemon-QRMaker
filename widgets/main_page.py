from utils.qr_core import *
from widgets.common.TextField import *
from widgets.common.Tab import *
from widgets.common.Dropdown import *
from widgets.common.Checkbox import *
from widgets.common.DateTime import *


class App(ft.Row):
    def __init__(self):
        super().__init__()
        
        self.qr = QRGenerator()
        self.data: str = None
        self.start_time: str = None

        """ --- TextField --- """
        url_txt.on_change = self.regenerate_preview
        filled_txt.on_change = self.regenerate_preview
        mail_txt.on_change = self.regenerate_preview
        subject_txt.on_change = self.regenerate_preview
        msg_txt.on_change = self.regenerate_preview
        phone_txt.on_change = self.regenerate_preview
        name_txt.on_change = self.regenerate_preview
        lastname_txt.on_change = self.regenerate_preview
        org_txt.on_change = self.regenerate_preview
        pos_txt.on_change = self.regenerate_preview
        work_phone_txt.on_change = self.regenerate_preview
        priv_phone_txt.on_change = self.regenerate_preview
        work_fax_txt.on_change = self.regenerate_preview
        priv_fax_txt.on_change = self.regenerate_preview
        street_txt.on_change = self.regenerate_preview
        zip_txt.on_change = self.regenerate_preview
        city_txt.on_change = self.regenerate_preview
        state_txt.on_change = self.regenerate_preview
        country_txt.on_change = self.regenerate_preview
        nickname_txt.on_change = self.regenerate_preview
        latitude_txt.on_change = self.regenerate_preview
        longitude_txt.on_change = self.regenerate_preview
        ssid_txt.on_change = self.regenerate_preview
        pass_txt.on_change = self.regenerate_preview
        title_txt.on_change = self.regenerate_preview
        location_txt.on_change = self.regenerate_preview
        app_txt.on_change = self.regenerate_preview
        crypto_address_txt.on_change = self.regenerate_preview
        amount_txt.on_change = self.regenerate_preview
        id_txt.on_change = self.regenerate_preview
        item_name_txt.on_change = self.regenerate_preview
        item_id_txt.on_change = self.regenerate_preview
        price_txt.on_change = self.regenerate_preview
        currency_txt.on_change = self.regenerate_preview
        ship_txt.on_change = self.regenerate_preview
        tax_txt.on_change = self.regenerate_preview
        border_txt.on_change = self.regenerate_preview
        fore_color_txt.on_change = self.regenerate_preview
        back_color_txt.on_change = self.regenerate_preview
        thanks_url_txt.on_change = self.regenerate_preview
        cancel_url_txt.on_change = self.regenerate_preview
        
        """ --- Dropdown --- """
        vcard_ver.on_change = self.regenerate_preview
        encrypt_drop.on_change = self.regenerate_preview
        crypto_drop.on_change = self.regenerate_preview
        payment_drop.on_change = self.regenerate_preview
        correction_drop.on_change = self.regenerate_preview
        
        """ --- Checkbox --- """
        hidden_check.on_change = self.regenerate_preview
        ver_auto_box.on_change = self.switch_version
        #custom_eye = self.regenerate_preview
        
        start_date_picker.on_change = self.get_start_datetime
        end_date_picker.on_change = self.get_end_datetime



        
        start_date.on_click = lambda e: self.page.open(
            ft.CupertinoBottomSheet(
                start_date_picker,
                height=216,
                padding=ft.padding.only(top=6)
            )
        )
        end_date.on_click = lambda e: self.page.open(
            ft.CupertinoBottomSheet(
                end_date_picker,
                height=216,
                padding=ft.padding.only(top=6)
            )
        )
        # ------------------------------------

        self.cont = ft.Container(url_txt, padding=10, width=750)
        self.tabs_widget_container = ft.Container(ft.Column([tab_row, self.cont]), alignment=ft.alignment.top_left, width=770)

        # --- Size Section ---
        self.version_slider = ft.Slider(1, "{value}", 1, 40, 39, on_change=self.regenerate_preview, disabled=True)
        
        self.size_row = ft.Row([self.version_slider, ver_auto_box])
        
        self.size_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("SET SIZE")),
                            ft.Container(ft.Column([self.size_row, border_txt]), 20),)])

        # --- Color Section ---
        self.color_radio_group = ft.RadioGroup(ft.Row(
                [
                    ft.Radio("Single Color", value="normal"),
                    ft.Radio("Color Gradient", value="gradient")
                ]
            ), "normal"
        )
        
        self.fore_color_row = ft.Row([fore_color_txt])
        self.color_column = ft.Column([self.color_radio_group, custom_eye, self.fore_color_row, back_color_txt])
        
        self.color_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("SET COLORS")), 
                            ft.Container(self.color_column, 20))])

        # --- Logo Section ---
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.open_logo = ft.ElevatedButton("Upload Logo", ft.icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "svg", "webp"]))
        self.delete_logo = ft.ElevatedButton("Delete Logo", ft.icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                            on_click=self.remove_logo, disabled=True)
        self.logo = ft.Image("Assets/logo.jpg", width=250, height=250)
        
        self.logo_row = ft.Row([self.open_logo, self.delete_logo], ft.MainAxisAlignment.CENTER, height=50)
        self.logo_column = ft.Column([self.logo, self.logo_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.logo_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("ADD LOGO IMAGE")),
                            ft.Container(self.logo_column, 20))])

        self.design_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("CUSTOM DESIGN")),
                            ft.Container( padding=20))])
        
        self.advanced_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("ADVANCED SETTINGS")),
                            ft.Container(correction_drop, 20))])

        # --- Right Layout ---
        self.save_file_dialog = ft.FilePicker(on_result=self.save_file_result)
        self.save_btn = ft.ElevatedButton("Save", ft.icons.SAVE,
                            on_click=lambda _: self.save_file_dialog.save_file(file_type=ft.FilePickerFileType.IMAGE))
        
        self.qr_size_slider = ft.Slider(50, "{value}", 10, 100, 9, on_change=self.update_scale_txt)

        self.qr_preview = ft.Image(src_base64=self.build_qr(), width=400, height=400)
        self.prev_container = ft.Container(self.qr_preview, alignment=ft.alignment.top_center)

        self.scale_txt = ft.Text(self.qr.get_res(), weight=ft.FontWeight.BOLD)
        self.size_row = ft.Row([ft.Text("Low Quality"), self.scale_txt, ft.Text("High Quality")],
                            ft.MainAxisAlignment.SPACE_BETWEEN)
        self.right = ft.Container(ft.Column(
            [
                self.prev_container, self.qr_size_slider, 
                self.size_row, self.save_btn
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="white", width=500, height=1500)

        self.main = ft.Container(ft.Column([self.size_panel, self.color_panel, self.logo_panel,
                                            self.design_panel, self.advanced_panel]), width=750)
        
        tabs_widget.on_change = self.update
        back.on_click = self.go_back
        forward.on_click = self.go_forward
    
    def get_start_datetime(self, e):
        current_start_date = e.control.value.strftime('%Y/%m/%d %H:%M')
        current_start_date_Text.value = current_start_date
        self.regenerate_preview(e)
        self.update(e)

    def get_end_datetime(self, e):
        current_end_date = e.control.value.strftime('%Y/%m/%d %H:%M')
        current_end_date_Text.value = current_end_date
        self.regenerate_preview(e)
        self.update(e)
    
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

    def __manage_tabs(self):
        match tabs_widget.selected_index:
            case 0:
                reset_text(True)
                self.cont.content = url_txt
                back.visible = False

            case 1:
                reset_text()
                filled_txt.label = "Write your text here"
                self.cont.content = filled_txt

            case 2:
                reset_text()
                self.cont.content = ft.Column([mail_txt, subject_txt, msg_txt])

            case 3:
                reset_text()
                self.cont.content = phone_txt

            case 4:
                reset_text()
                self.cont.content = ft.Column([phone_txt, msg_txt])
                forward.visible = True
                
            case 5:
                reset_text()
                whatsapp_icon.color = ft.colors.PRIMARY
                self.cont.content = ft.Column([phone_txt, msg_txt])
                forward.visible = True

            case 6:
                card_pages()
                reset_drop()
                self.cont.content = ft.Column(
                    [
                        vcard_ver,
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
                card_pages()
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
                reset_text()
                self.cont.content = ft.Row([latitude_txt, longitude_txt])

            case 9:
                reset_text()
                reset_drop()
                self.cont.content = ft.Column(
                    [
                        ssid_txt,
                        pass_txt,
                        ft.Row([encrypt_drop, hidden_check]),
                    ]
                )
                        
            case 10:
                reset_text()
                self.cont.content = ft.Column(
                    [title_txt, 
                     location_txt, 
                     ft.Row([start_date, end_date]), 
                    ]
                )
            
            case 11:
                reset_text()
                self.cont.content = ft.Column([app_txt])

            case 12:
                reset_text(True)
                self.cont.content = ft.Column([title_txt, url_txt])

            case 13:
                reset_text()
                reset_drop()
                self.cont.content = ft.Column(
                    [
                        ft.Row([payment_drop, mail_txt]),
                        ft.Row([item_name_txt, item_id_txt]),
                        ft.Row([price_txt, currency_txt]),
                        ft.Row([ship_txt, tax_txt]),
                        ft.Row([thanks_url_txt, cancel_url_txt])
                    ]
                )

            case 14:
                reset_text()
                reset_drop()
                forward.visible = False
                self.cont.content = ft.Column(
                    [
                        crypto_drop,
                        crypto_address_txt,
                        amount_txt,
                        id_txt,
                        msg_txt,
                    ]
                )

            case _:
                forward.visible = True
    
    def update(self, e):
        self.__manage_tabs()

        if tabs_widget.selected_index != 5:
            whatsapp_icon.color = ft.colors.ON_BACKGROUND
        if tabs_widget.selected_index > 0:
            back.visible = True

        super().update()

    # --- QR Building ---
    def build_qr(self) -> str:
        wifi_encrypt: str = ""
        network_hide: str = ""
        vcard_txt: str = ""
        crypto_currency: str = ""
        start_dt: str = None
        end_dt: str = None

        match tabs_widget.selected_index:
            case 6:
                if vcard_ver.value == "Version 3":
                    vcard_txt = f"BEGIN:VCARD\nVERSION:3.0\nN:{lastname_txt.value};{name_txt.value}\nFN:{name_txt.value} {lastname_txt.value}\nTITLE:{pos_txt.value}\nORG:{org_txt.value}\nURL:{url_txt.value}\nEMAIL;TYPE=INTERNET:{mail_txt.value}\nTEL;TYPE=voice,work,pref:{work_phone_txt.value}\nTEL;TYPE=voice,home,pref:{priv_phone_txt.value}\nTEL;TYPE=voice,cell,pref:{phone_txt.value}\nTEL;TYPE=fax,work,pref:{work_fax_txt.value}\nTEL;TYPE=fax,home,pref:{priv_fax_txt.value}\nADR:;;{street_txt.value};{city_txt.value};{state_txt.value};{zip_txt.value};{country_txt.value}\nEND:VCARD"
                else:
                    vcard_txt = f"BEGIN:VCARD\nVERSION:2.1\nN:{lastname_txt.value};{name_txt.value}\nTITLE:{pos_txt.value}\nORG:{org_txt.value}\nURL:{url_txt.value}\nEMAIL;TYPE=INTERNET:{mail_txt.value}\nTEL;WORK;VOICE:{work_phone_txt.value}\nTEL;HOME;VOICE:{priv_phone_txt.value}\nTEL;CELL:{phone_txt.value}\nTEL;WORK;FAX:{work_fax_txt.value}\nTEL;HOME;FAX:{priv_fax_txt.value}\nADR:;;{street_txt.value};{city_txt.value};{state_txt.value};{zip_txt.value};{country_txt.value}\nEND:VCARD"                
            
            case 8:
                try:
                    latitude = float(latitude_txt.value)
                    if latitude > 90:
                        latitude_txt.value = "90"
                    if latitude < -90:
                        latitude_txt.value = "-90"
                    latitude_txt.update()
                except ValueError as e:
                    print(f"Latitude: {e}")
                    
                try:
                    longitude = float(longitude_txt.value)
                    if longitude > 180:
                        longitude_txt.value = "180"
                    if longitude < -180:
                        longitude_txt.value = "-180"
                    longitude_txt.update()
                except ValueError as e:
                    print(f"Longitude: {e}")

            case 9:
                wifi_encrypt_map = {"None": "nopass", "WEP": "WEP", "WPA/WPA2": "WPA"}
                wifi_encrypt = wifi_encrypt_map.get(encrypt_drop.value, None)
                network_hide = "true" if hidden_check.value else "false"

            case 10:
                start_dt = format(0)
                end_dt = format(1)

            case 14:
                crypto_currencies = {
                    "Bitcoin": "bitcoin",
                    "Bitcoin Cash": "bitcoincash",
                    "Ethereum": "ethereum",
                    "Litecoin": "litecoin",
                    "Dash": "dash",
                }
                crypto_currency = crypto_currencies.get(crypto_drop.value, None)
        
        qr_data_formats = {
            0: url_txt.value,
            1: filled_txt.value,
            2: f"mailto:{mail_txt.value}?subject={subject_txt.value}&body={msg_txt.value}",
            3: f"tel:{phone_txt.value}",
            4: f"SMSTO:{phone_txt.value}:{msg_txt.value}",
            5: f"https://wa.me/{phone_txt.value}/?text={msg_txt.value}",
            6: vcard_txt,
            7: f"MECARD:N:{lastname_txt.value},{name_txt.value};NICKNAME:{nickname_txt.value};TEL:{work_phone_txt.value};TEL:{priv_phone_txt.value};TEL:{phone_txt.value};EMAIL:{mail_txt.value};BDAY:;URL:{url_txt.value}NOTE:{filled_txt.value};ADR:,,{street_txt.value},{city_txt.value},{state_txt.value},{zip_txt.value},{country_txt.value};;",
            8: f"https://maps.google.com/local?q={latitude_txt.value},{longitude_txt.value}",
            9: f"WIFI:S:{ssid_txt.value};T:{wifi_encrypt};P:{pass_txt.value};H:{network_hide};;",
            10: f"BEGIN:VEVENT\nUID:{title_txt.value}\nORGANIZER:\nSUMMARY:\nLOCATION:{location_txt.value}\nDTSTART:{start_dt}\nDTEND:{end_dt}\nEND:VEVENT",
            11: f"market://details?id={app_txt.value}",
            12: f"MEBKM:TITLE:{title_txt.value};URL:{url_txt.value};;",
            13: f"https://www.paypal.com/cgi-bin/webscr?business={mail_txt.value}&cmd=_xclick&currency_code={currency_txt.value}&amount={price_txt.value}&item_name={item_name_txt.value}&return={thanks_url_txt.value}&cancel_return={cancel_url_txt.value}",
            14: f"{crypto_currency}:{id_txt.value}?amount={amount_txt.value}&message={msg_txt.value}",
        }
        self.qr.data = qr_data_formats.get(tabs_widget.selected_index, None)

        self.qr.version = None if ver_auto_box.value else int(self.version_slider.value)
        self.qr.box_size = int(self.qr_size_slider.value)
        self.qr.border = 4 if border_txt.value == "" else int(border_txt.value)
        self.qr.back_color = back_color_txt.value
        self.qr.main_color = fore_color_txt.value
        
        return self.qr.generate_preview()

    # --- Realtime Building ---
    def regenerate_preview(self, e):
        self.qr_preview.src_base64 = self.build_qr()
        self.qr_preview.update()

    def switch_version(self, e):
        if ver_auto_box.value:
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
                ft.ft.Text(f"Image saved in {e.path}"),
                True,
                bgcolor=ft.colors.GREEN,
            )
            self.page.update()

    def build(self):
        return ft.Row(
            [
                ft.Column(
                    [self.tabs_widget_container, self.main],
                    height=650,
                    scroll=ft.ScrollMode.ADAPTIVE,
                ),
                self.right
            ],
            ft.MainAxisAlignment.CENTER, ft.CrossAxisAlignment.START
        )

    def did_mount(self):
        self.page.overlay.extend([self.save_file_dialog, self.pick_files_dialog])
        self.page.update()