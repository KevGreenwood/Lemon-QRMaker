from shelve import Shelf

from utils.qr_core import *
from widgets.common.TextField import *
from widgets.common.Tab import *
from widgets.common.Dropdown import *
from widgets.common.Checkbox import *
from widgets.common.DateTime import *
from widgets.common.ColorPicker import *
from widgets.common.ShapeButton import *

class App(ft.Row):
    def __init__(self):
        super().__init__()
        
        self.qr = QRGenerator()
        self.start_datetime: str = ""
        self.end_datetime: str = ""
        self.birthday: str = ""

        """ --- Buttons --- """
        squarebody_Button.on_click = self.normalDrawer
        gappedbody_Button.on_click = self.gappedDrawer
        circlebody_Button.on_click = self.circleDrawer
        roundedbody_Button.on_click = self.roundedDrawer
        verticalbody_Button.on_click = self.verticalDrawer
        horizontalbody_Button.on_click = self.horizontalDrawer
        squareeye_Button.on_click = self.normalDrawer_eye
        gappedeye_Button.on_click = self.gappedDrawer_eye
        circleeye_Button.on_click = self.circleDrawer_eye
        roundedeye_Button.on_click = self.roundedDrawer_eye
        verticaleye_Button.on_click = self.verticalDrawer_eye
        horizontaleye_Button.on_click = self.horizontalDrawer_eye

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
        organizer_txt.on_change = self.regenerate_preview
        summary_txt.on_change = self.regenerate_preview
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
        thanks_url_txt.on_change = self.regenerate_preview
        cancel_url_txt.on_change = self.regenerate_preview
        
        """ --- Dropdown --- """
        vcard_ver.on_change = self.regenerate_preview
        encrypt_drop.on_change = self.regenerate_preview
        crypto_drop.on_change = self.regenerate_preview
        payment_drop.on_change = self.regenerate_preview
        correction_drop.on_change = self.regenerate_preview
        gradiant_drop.on_change = self.switch_gradients
        #inner_eye_gradiant_drop.on_change = self.manage_eye_color_style
        #outer_eye_gradiant_drop.on_change = self.manage_eye_color_style

        """ --- Checkbox --- """
        hidden_check.on_change = self.regenerate_preview
        ver_auto_box.on_change = self.switch_version
        #custom_eye.on_change = self.manage_eye_style
        
        """ --- DatePicker --- """
        start_dt_Picker.on_change = self.get_start_datetime
        end_dt_Picker.on_change = self.get_end_datetime


        background_Button.fx =  self.regenerate_preview
        foreground_Button.fx = self.regenerate_preview
        gradient_Button.fx = self.regenerate_preview
        #inner_eye_Button.fx = self.regenerate_preview
        #inner_eye_gradient_Button.fx = self.regenerate_preview
        #outer_eye_Button.fx = self.regenerate_preview
        #outer_eye_gradient_Button.fx = self.regenerate_preview

        start_dt_Button.on_click = lambda e: self.page.open(
            ft.CupertinoBottomSheet(
                start_dt_Picker,
                height=216,
                padding=ft.padding.only(top=6)
            )
        )
        end_dt_Button.on_click = lambda e: self.page.open(
            ft.CupertinoBottomSheet(
                end_dt_Picker,
                height=216,
                padding=ft.padding.only(top=6)
            )
        )
        birthday_Button.on_click = lambda e: self.page.open(
            ft.DatePicker(on_change=self.get_birthday)
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
            ), "normal", self.manage_color_style
        )
        self.fore_color_row = ft.Row([foreground_Button])
        #self.color_radio_group, custom_eye
        self.color_column = ft.Column([ft.Row([self.color_radio_group,]), self.fore_color_row, background_Button])
        
        self.color_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("SET COLORS")), 
                            ft.Container(self.color_column, 20))])

        # --- Logo Section ---
        self.pick_files_dialog = ft.FilePicker(self.pick_files_result)
        self.open_logo = ft.ElevatedButton("Upload Logo", ft.Icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "svg", "webp"]))
        self.delete_logo = ft.ElevatedButton("Delete Logo", ft.Icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                            on_click=self.remove_logo, disabled=True)
        self.logo = ft.Image("Assets/logo.jpg", width=250, height=250)
        
        self.logo_row = ft.Row([self.open_logo, self.delete_logo], ft.MainAxisAlignment.CENTER, height=50)
        self.logo_column = ft.Column([self.logo, self.logo_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.logo_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("ADD LOGO IMAGE")),
                            ft.Container(self.logo_column, 20))])


        self.pick_image_dialog = ft.FilePicker(self.pick_image_result)
        self.open_image = ft.ElevatedButton("Upload Image", ft.Icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_image_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "svg", "webp"]))
        self.delete_image = ft.ElevatedButton("Delete Image", ft.Icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                            on_click=self.remove_image, disabled=True)
        self.image = ft.Image("Assets/logo.jpg", width=250, height=250)

        self.image_row = ft.Row([self.open_image, self.delete_image], ft.MainAxisAlignment.CENTER, height=50)
        self.image_column = ft.Column([self.image, self.image_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


        self.body_Column = ft.Column(
            [
                ft.Text("Body Shapes"),
                ft.Row(
                    [squarebody_Button, gappedbody_Button, circlebody_Button, roundedbody_Button, verticalbody_Button,
                     horizontalbody_Button], wrap=True),

            ]
        )

        self.eyes_Column = ft.Column(
            [
                ft.Text("Eyes Shapes"),
                ft.Row(
                    [squareeye_Button, gappedeye_Button, circleeye_Button, roundedeye_Button, verticaleye_Button,
                     horizontaleye_Button], wrap=True)

            ]
        )

        self.design_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("CUSTOM DESIGN")),
                            ft.Container(ft.Column([self.body_Column, self.eyes_Column]), padding=20))])

        self.advanced_panel = ft.ExpansionPanelList([ft.ExpansionPanel(ft.ListTile(title=ft.Text("ADVANCED SETTINGS")),
                            ft.Container(correction_drop, 20))])

        # --- Right Layout ---
        self.save_file_dialog = ft.FilePicker(on_result=self.save_file_result)
        self.save_btn = ft.ElevatedButton("Save", ft.Icons.SAVE,
                            on_click=lambda _: self.save_file_dialog.save_file(file_type=ft.FilePickerFileType.IMAGE))
        
        self.qr_size_slider = ft.Slider(32, "{value}", 10, 55, on_change=self.update_scale_txt)

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

        """
        self.inner_eye_row = ft.Row([inner_eye_Button, inner_eye_gradiant_drop])
        self.outer_eye_row = ft.Row([outer_eye_Button, outer_eye_gradiant_drop])
        self.eye_column = ft.Column([self.inner_eye_row, self.outer_eye_row])
        """

        self.qr_colors_row = ft.Row([gradient_Button, gradiant_drop])
        
        tabs_widget.on_change = self.update
        back.on_click = self.go_back
        forward.on_click = self.go_forward

    """
        def manage_eye_color_style(self, e):
        if inner_eye_gradiant_drop.value != "Solid Color":
            self.inner_eye_row.controls.append(inner_eye_gradient_Button)
            self.qr.inner_use_gradiant = True
        else:
            self.inner_eye_row.controls.remove(inner_eye_gradient_Button)
            self.qr.inner_use_gradiant = False
        
        if outer_eye_gradiant_drop.value != "Solid Color":
            self.outer_eye_row.controls.append(outer_eye_gradient_Button)
            self.qr.outer_use_gradiant = True
        else:
            self.outer_eye_row.controls.remove(outer_eye_gradient_Button)
            self.qr.outer_use_gradiant = False
        self.regenerate_preview(e)
        self.page.update()
    """
    def normalDrawer(self, e):
        self.qr.bodyDrawer_index = 0
        self.regenerate_preview(e)

    def gappedDrawer(self, e):
        self.qr.bodyDrawer_index = 1
        self.regenerate_preview(e)

    def circleDrawer(self, e):
        self.qr.bodyDrawer_index = 2
        self.regenerate_preview(e)

    def roundedDrawer(self, e):
        self.qr.bodyDrawer_index = 3
        self.regenerate_preview(e)

    def verticalDrawer(self, e):
        self.qr.bodyDrawer_index = 4
        self.regenerate_preview(e)

    def horizontalDrawer(self, e):
        self.qr.bodyDrawer_index = 5
        self.regenerate_preview(e)


    def normalDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 0
        self.regenerate_preview(e)

    def gappedDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 1
        self.regenerate_preview(e)

    def circleDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 2
        self.regenerate_preview(e)

    def roundedDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 3
        self.regenerate_preview(e)

    def verticalDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 4
        self.regenerate_preview(e)

    def horizontalDrawer_eye(self, e):
        self.qr.eyeDrawer_index = 5
        self.regenerate_preview(e)

    
    def manage_color_style(self, e):
        if self.color_radio_group.value == "gradient":
            self.fore_color_row.controls.append(self.qr_colors_row)
            self.qr.use_gradiant = True
        else:
            self.fore_color_row.controls.remove(self.qr_colors_row)
            self.qr.use_gradiant = False
        self.regenerate_preview(e)
        self.page.update()

    """
        def manage_eye_style(self, e):
        if custom_eye.value:
            self.color_column.controls.append(self.eye_column)
        else:
            self.color_column.controls.remove(self.eye_column)
        self.regenerate_preview(e)
        self.page.update()
    """

    def get_start_datetime(self, e):
        self.start_datetime = e.control.value.strftime("%Y%m%dT%H%M")
        start_dt_Text.value = e.control.value.strftime('%Y/%m/%d %H:%M')
        self.regenerate_preview(e)
        start_dt_Text.update()

    def get_end_datetime(self, e):
        self.end_datetime = e.control.value.strftime("%Y%m%dT%H%M")
        end_dt_Text.value = e.control.value.strftime('%Y/%m/%d %H:%M')
        self.regenerate_preview(e)
        end_dt_Text.update()
    
    def get_birthday(self, e):
        self.birthday = e.control.value.strftime("%Y%m%d")
        birthday_Text.value = e.control.value.strftime('%Y/%m/%d')
        self.regenerate_preview(e)
        birthday_Text.update()

    # Custom ft.Tabs
    def go_back(self, e):
        if tabs_widget.selected_index > 0:
            tabs_widget.selected_index -= 1
            #back.icon_color = ft.Colors.ON_SURFACE
        self.update(e)

    def go_forward(self, e):
        if tabs_widget.selected_index < 14:
            tabs_widget.selected_index += 1
            forward.icon_color = ft.Colors.ON_SURFACE
        self.update(e)

    def __manage_tabs(self):
        match tabs_widget.selected_index:
            case 0:
                reset_text(True)
                self.cont.content = url_txt

            case 1:
                reset_text()
                filled_txt.label = "Write your text here"
                self.cont.content = filled_txt

            case 2:
                reset_text()
                mail_txt.width = None
                self.cont.content = ft.Column([mail_txt, subject_txt, msg_txt])

            case 3:
                reset_text()
                self.cont.content = phone_txt

            case 4:
                reset_text()
                phone_txt.width = None
                self.cont.content = ft.Column([phone_txt, msg_txt])
                
            case 5:
                reset_text()
                whatsapp_icon.color = ft.Colors.PRIMARY
                phone_txt.width = None
                self.cont.content = ft.Column([phone_txt, msg_txt])

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
                        ft.Row([street_txt, birthday_Button]),
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
                     organizer_txt,
                     summary_txt,
                     ft.Row([start_dt_Button, end_dt_Button]), 
                    ]
                )
            
            case 11:
                reset_text()
                self.cont.content = ft.Column([app_txt])

            case 12:
                reset_text(True)
                url_txt.width = None
                self.cont.content = ft.Column([title_txt, url_txt])

            case 13:
                reset_text()
                reset_drop()
                mail_txt.width = 360
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
                self.cont.content = ft.Column(
                    [
                        crypto_drop,
                        crypto_address_txt,
                        amount_txt,
                        id_txt,
                        msg_txt,
                    ]
                )
    
    def update(self, e):
        self.__manage_tabs()

        if tabs_widget.selected_index != 5:
            whatsapp_icon.color = ft.Colors.ON_SURFACE
            
        if tabs_widget.selected_index > 0:
            back.disabled = False
        else:
            back.disabled = True

        if tabs_widget.selected_index < 14:
            forward.disabled = False
        else:
            forward.disabled = True

        super().update()

    # --- QR Building ---
    def build_qr(self) -> str:
        wifi_encrypt: str = ""
        network_hide: str = ""
        vcard_txt: str = ""
        crypto_currency: str = ""
        gradiant_style_map = {"Radial Gradient": 1, "Square Gradient": 2, "Horizontal Gradient": 3, "Vertical Gradient": 4, "Image Fill": 5}

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
            7: f"MECARD:N:{lastname_txt.value},{name_txt.value};NICKNAME:{nickname_txt.value};TEL:{work_phone_txt.value};TEL:{priv_phone_txt.value};TEL:{phone_txt.value};EMAIL:{mail_txt.value};BDAY:{self.birthday};URL:{url_txt.value}NOTE:{filled_txt.value};ADR:,,{street_txt.value},{city_txt.value},{state_txt.value},{zip_txt.value},{country_txt.value};;",
            8: f"https://maps.google.com/local?q={latitude_txt.value},{longitude_txt.value}",
            9: f"WIFI:S:{ssid_txt.value};T:{wifi_encrypt};P:{pass_txt.value};H:{network_hide};;",
            10: f"BEGIN:VEVENT\nUID:{title_txt.value}\nORGANIZER:{organizer_txt.value}\nLOCATION:{location_txt.value}\nDTSTART:{self.start_datetime}\nDTEND:{self.end_datetime}\nSUMMARY:{summary_txt.value}\nEND:VEVENT",
            11: f"market://details?id={app_txt.value}",
            12: f"MEBKM:TITLE:{title_txt.value};URL:{url_txt.value};;",
            13: f"https://www.paypal.com/cgi-bin/webscr?business={mail_txt.value}&cmd=_xclick&currency_code={currency_txt.value}&amount={price_txt.value}&item_name={item_name_txt.value}&return={thanks_url_txt.value}&cancel_return={cancel_url_txt.value}",
            14: f"{crypto_currency}:{id_txt.value}?amount={amount_txt.value}&message={msg_txt.value}",
        }
        self.qr.data = qr_data_formats.get(tabs_widget.selected_index, None)

        self.qr.version = None if ver_auto_box.value else int(self.version_slider.value)
        self.qr.real_box_size = int(self.qr_size_slider.value)
        self.qr.border = 4 if border_txt.value == "" else int(border_txt.value)

        self.qr.back_color = background_Button.qr_color
        self.qr.main_color = foreground_Button.qr_color
        """
        if custom_eye.value:
            self.qr.custom_eye_color = True
            self.qr.main_color_inner_eyes = inner_eye_Button.qr_color
            self.qr.main_color_outer_eyes = outer_eye_Button.qr_color
        else:
            self.qr.custom_eye_color = False
        """


        error_correction_map = {"Low": 0, "Medium": 1, "High": 2, "Very High": 3}
        error_correction = error_correction_map.get(correction_drop.value, None)
        if self.qr.use_logo:
            correction_drop.value = "High"
            correction_drop.update()
            self.qr.error_correction = 2
        else:
            self.qr.error_correction = error_correction

        if self.color_radio_group.value == "gradient":
            self.qr.alt_color = gradient_Button.qr_color
            self.qr.colorMask_index = gradiant_style_map.get(gradiant_drop.value, None)


        """
                if inner_eye_gradiant_drop.value != "Solid Color":
            self.qr.alt_color_inner_eyes = inner_eye_gradient_Button.qr_color
            self.qr.colorMask_index = gradiant_style_map.get(inner_eye_gradiant_drop.value, None)
        
        if outer_eye_gradiant_drop.value != "Solid Color":
            self.qr.alt_color_outer_eyes = outer_eye_gradient_Button.qr_color
            self.qr.colorMask_index = gradiant_style_map.get(outer_eye_gradiant_drop.value, None)
        """

        
        return self.qr.generate_preview()

    def switch_gradients(self, e):
        if gradiant_drop.value == "Image Fill":
            self.color_column.controls.append(self.image_column)
        else:
            self.color_column.controls.remove(self.image_column)

        self.page.update()

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
            self.qr.logo_path = ""
            self.qr.use_logo = False
            correction_drop.value = "Low"
            correction_drop.update()
            self.logo.src = "assets/logo.jpg"
            self.logo.update()
            self.regenerate_preview(e)
            self.delete_logo.disabled = True
            self.delete_logo.update()


    def remove_image(self, e):
        if not self.delete_image.disabled:
            self.qr.img_fill_path = ""
            correction_drop.value = "Low"
            correction_drop.update()
            self.image.src = "assets/logo.jpg"
            self.image.update()
            #self.regenerate_preview(e)
            self.delete_image.disabled = True
            self.delete_image.update()

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

    def pick_image_result(self, e: ft.FilePickerResultEvent):
        if e.files:  # Prevents Error if you cancel
            for file in e.files:
                print("Nombre del archivo:", file.name)
                print("Ruta del archivo:", file.path)
                print("Tamaño del archivo:", file.size)
            self.image.src = e.files[0].path
            self.qr.img_fill_path = e.files[0].path
            self.image.update()
            self.regenerate_preview(e)
            self.delete_image.disabled = False
            self.delete_image.update()

    def save_file_result(self, e: ft.FilePickerResultEvent):
        if e.path:  # Prevents save a filename named "None" in the app path
            self.qr.generate_final(e.path)

            print(f"Image saved in {e.path}")

            self.page.overlay.append(ft.SnackBar(
                ft.Text(f"Image saved in {e.path}"),
                True,
                bgcolor=ft.Colors.GREEN,
            ))
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
        self.page.overlay.extend([self.save_file_dialog, self.pick_files_dialog, self.pick_image_dialog])
        self.page.update()