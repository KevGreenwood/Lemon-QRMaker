from flet.core.responsive_row import ResponsiveRow
from flet.core.vertical_divider import VerticalDivider

from widgets.Radio import *
from utils.qr_core import QRGenerator
from widgets.TextField import *
from widgets.Tab import *
from widgets.Dropdown import *
from widgets.Checkbox import *
from widgets.DateTime import *
from widgets.ColorPicker import *
from widgets.ShapeButton import *
from flet import (CupertinoBottomSheet, Container, SnackBar, FilePicker, FilePickerResultEvent, DatePicker, Slider, ExpansionPanel, ExpansionPanelList, ListTile, RadioGroup, Radio, FilePickerFileType, FontWeight, ScrollMode, alignment, padding)


class App(Row):
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


        start_dt_Button.on_click = lambda e: self.page.open(
            CupertinoBottomSheet(
                start_dt_Picker,
                height=216,
                padding=padding.only(top=6)
            )
        )
        end_dt_Button.on_click = lambda e: self.page.open(
            CupertinoBottomSheet(
                end_dt_Picker,
                height=216,
                padding=padding.only(top=6)
            )
        )
        birthday_Button.on_click = lambda e: self.page.open(
            DatePicker(on_change=self.get_birthday)
        )


        gradiant_drop.on_change = self.switch_gradients
        #inner_eye_gradiant_drop.on_change = self.manage_eye_color_style
        #outer_eye_gradiant_drop.on_change = self.manage_eye_color_style

        """ --- Checkbox --- """
        ver_auto_box.on_change = self.switch_version
        #custom_eye.on_change = self.manage_eye_style
        
        """ --- DatePicker --- """
        start_dt_Picker.on_change = self.get_start_datetime
        end_dt_Picker.on_change = self.get_end_datetime

        # ------------------------------------

        self.cont = Container(url_txt, padding=10, width=750)
        self.tabs_widget_container = Container(Column([tab_row]), alignment=alignment.top_left, width=770)
        # --- Size Section ---
        self.version_slider = Slider(1, "{value}", 1, 40, 39, disabled=True)
        
        self.size_row = Row([self.version_slider, ver_auto_box])
        
        self.size_panel = ExpansionPanelList([ExpansionPanel(ListTile(title=Text("SET SIZE")),
                            Container(Column([self.size_row, border_txt]), 20),)])

        # --- Color Section ---
        color_radio_group.on_change = self.manage_color_style


        self.fore_color_row = Row([foreground_Button])
        self.color_column = Column([Row([color_radio_group]), self.fore_color_row, background_Button])
        
        self.color_panel = ExpansionPanelList([ExpansionPanel(ListTile(title=Text("SET COLORS")), 
                            Container(self.color_column, 20))])

        # --- Logo Section ---
        self.pick_files_dialog = FilePicker(self.pick_files_result)
        self.open_logo = ElevatedButton("Upload Logo", Icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "webp"]))
        self.delete_logo = ElevatedButton("Delete Logo", Icons.REMOVE_CIRCLE_OUTLINE_ROUNDED,
                            on_click=self.remove_logo, disabled=True)
        self.logo = Image("/placeholder.svg", width=250, height=250)
        
        self.logo_row = Row([self.open_logo, self.delete_logo], MainAxisAlignment.CENTER, height=50)
        self.logo_column = Column([self.logo, self.logo_row], horizontal_alignment=CrossAxisAlignment.CENTER)
        
        self.logo_panel = ExpansionPanelList([ExpansionPanel(ListTile(title=Text("ADD LOGO IMAGE")),
                            Container(self.logo_column, 20))])


        self.pick_image_dialog = FilePicker(self.pick_image_result)
        self.open_image = ElevatedButton("Upload Image", Icons.UPLOAD_FILE_ROUNDED,
            on_click=lambda _: self.pick_image_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg", "jpg", "svg", "webp"]))
        self.image = Image("/placeholder.svg", width=250, height=250)
        self.image_column = Row([Column([self.image, self.open_image], horizontal_alignment=CrossAxisAlignment.CENTER)], alignment=MainAxisAlignment.CENTER)


        self.body_Column = Column(
            [
                Text("Body Shapes"),
                Row(
                    [squarebody_Button, gappedbody_Button, circlebody_Button, roundedbody_Button, verticalbody_Button,
                     horizontalbody_Button], wrap=True),

            ]
        )

        self.eyes_Column = Column(
            [
                Text("Eyes Shapes"),
                Row(
                    [squareeye_Button, gappedeye_Button, circleeye_Button, roundedeye_Button, verticaleye_Button,
                     horizontaleye_Button], wrap=True)

            ]
        )

        self.design_panel = ExpansionPanelList([ExpansionPanel(ListTile(title=Text("CUSTOM DESIGN")),
                            Container(Column([self.body_Column, self.eyes_Column]), padding=20))])

        self.advanced_panel = ExpansionPanelList([ExpansionPanel(ListTile(title=Text("ADVANCED SETTINGS")),
                            Container(correction_drop, 20))])

        # --- Right Layout ---
        self.save_file_dialog = FilePicker(on_result=self.save_file_result)
        self.save_btn = ElevatedButton("Save", Icons.SAVE,
                            on_click=lambda _: self.save_file_dialog.save_file(file_name="qr.png", allowed_extensions=["png", "jpeg", "jpg", "webp"]))
        self.gen_btn = ElevatedButton("Generate", Icons.QR_CODE,
                                       on_click=self.regenerate_preview)
        self.button_row = Row([self.gen_btn, self.save_btn], alignment=MainAxisAlignment.CENTER, spacing=40, )


        self.qr_size_slider = Slider(32, "{value}", 10, 55, on_change=self.update_scale_txt)
        self.qr_preview = Image(src_base64=self.build_qr(), width=400, height=400)
        self.prev_container = Container(self.qr_preview, alignment=alignment.top_center)

        self.scale_txt = Text(self.qr.get_res(), weight=FontWeight.BOLD)
        self.size_row = Row([Text("      Low Quality"), self.scale_txt, Text("High Quality      ")],
                            MainAxisAlignment.SPACE_BETWEEN)
        self.right = Column(
            [
                self.prev_container, self.qr_size_slider, 
                self.size_row, self.button_row
            ], horizontal_alignment=CrossAxisAlignment.CENTER, col={"sm": 12, "md": 5, "lg": 4})

        self.main = Column([self.cont, self.size_panel, self.color_panel, self.logo_panel,
                                            self.design_panel, self.advanced_panel], col={"sm": 12, "md": 7, "lg": 8})

        """
        self.inner_eye_row = Row([inner_eye_Button, inner_eye_gradiant_drop])
        self.outer_eye_row = Row([outer_eye_Button, outer_eye_gradiant_drop])
        self.eye_column = Column([self.inner_eye_row, self.outer_eye_row])
        """

        self.qr_colors_row = Row([gradient_Button, gradiant_drop])
        
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
        match color_radio_group.value:
            case "normal":
                self.qr.use_gradiant = False
                self.qr.colorMask_index = 0
                gradiant_drop.value = "Radial Gradient"
                foreground_Button.disabled = False
                if self.qr_colors_row in self.fore_color_row.controls:
                    self.fore_color_row.controls.remove(self.qr_colors_row)
                if self.image_column in self.color_column.controls:
                    self.color_column.controls.remove(self.image_column)
                    self.image.src = "/placeholder.svg"

            case "gradient":
                if not self.qr_colors_row in self.fore_color_row.controls:
                    self.fore_color_row.controls.append(self.qr_colors_row)
                self.qr.use_gradiant = True
                self.qr.colorMask_index = 1
                gradiant_drop.value = "Radial Gradient"
                foreground_Button.disabled = False
                gradient_Button.disabled = False
                if self.image_column in self.color_column.controls:
                    self.color_column.controls.remove(self.image_column)
                    self.image.src = "/placeholder.svg"

            case "image":
                if self.qr_colors_row in self.fore_color_row.controls:
                    self.fore_color_row.controls.remove(self.qr_colors_row)
                if not self.image_column in self.color_column.controls:
                    gradient_Button.disabled = True
                    foreground_Button.disabled = True
                    self.color_column.controls.append(self.image_column)

        self.page.update()

    """
        def manage_eye_style(self, e):
        if custom_eye.value:
            self.color_column.controls.append(self.eye_column)
        else:
            self.color_column.controls.remove(self.eye_column)
        self.page.update()
    """

    def get_start_datetime(self, e):
        self.start_datetime = e.control.value.strftime("%Y%m%dT%H%M")
        start_dt_Text.value = e.control.value.strftime('%Y/%m/%d %H:%M')
        start_dt_Text.update()

    def get_end_datetime(self, e):
        self.end_datetime = e.control.value.strftime("%Y%m%dT%H%M")
        end_dt_Text.value = e.control.value.strftime('%Y/%m/%d %H:%M')
        end_dt_Text.update()
    
    def get_birthday(self, e):
        self.birthday = e.control.value.strftime("%Y%m%d")
        birthday_Text.value = e.control.value.strftime('%Y/%m/%d')
        birthday_Text.update()

    # Custom Tabs
    def go_back(self, e):
        if tabs_widget.selected_index > 0:
            tabs_widget.selected_index -= 1
            #back.icon_color = Colors.ON_SURFACE
        self.update(e)

    def go_forward(self, e):
        if tabs_widget.selected_index < 14:
            tabs_widget.selected_index += 1
            forward.icon_color = Colors.ON_SURFACE
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
                self.cont.content = Column([mail_txt, subject_txt, msg_txt])
            case 3:
                reset_text()
                self.cont.content = phone_txt
            case 4:
                reset_text()
                phone_txt.width = None
                self.cont.content = Column([phone_txt, msg_txt])
            case 5:
                reset_text()
                whatsapp_icon.color = Colors.PRIMARY
                phone_txt.width = None
                self.cont.content = Column([phone_txt, msg_txt])
            case 6:
                card_pages()
                reset_drop()
                self.cont.content = Column(
                    [
                        vcard_ver_group,
                        Row([name_txt, lastname_txt]),
                        Row([org_txt, pos_txt]),
                        Row([work_phone_txt, priv_phone_txt]),
                        Row([phone_txt, work_fax_txt]),
                        Row([priv_fax_txt, mail_txt]),
                        Row([url_txt, street_txt]),
                        Row([zip_txt, city_txt]),
                        Row([state_txt, country_txt]),
                    ]
                )
            case 7:
                card_pages()
                self.cont.content = Column(
                    [
                        Row([name_txt, lastname_txt]),
                        Row([nickname_txt, work_phone_txt]),
                        Row([priv_phone_txt, phone_txt]),
                        Row([mail_txt, url_txt]),
                        Row([street_txt, birthday_Button]),
                        Row([zip_txt, city_txt]),
                        Row([state_txt, country_txt]),
                        filled_txt,
                    ]
                )
            case 8:
                reset_text()
                self.cont.content = Row([latitude_txt, longitude_txt])
            case 9:
                reset_text()
                reset_drop()
                self.cont.content = Column(
                    [
                        ssid_txt,
                        pass_txt,
                        Row([encrypt_drop, hidden_check]),
                    ]
                )
            case 10:
                reset_text()
                self.cont.content = Column(
                    [title_txt, 
                     location_txt, 
                     organizer_txt,
                     summary_txt,
                     Row([start_dt_Button, end_dt_Button]), 
                    ]
                )
            case 11:
                reset_text()
                self.cont.content = Column([app_txt])
            case 12:
                reset_text(True)
                url_txt.width = None
                self.cont.content = Column([title_txt, url_txt])
            case 13:
                reset_text()
                reset_drop()
                mail_txt.width = 360
                self.cont.content = Column(
                    [
                        Row([payment_drop, mail_txt]),
                        Row([item_name_txt, item_id_txt]),
                        Row([price_txt, currency_txt]),
                        Row([ship_txt, tax_txt]),
                        Row([thanks_url_txt, cancel_url_txt])
                    ]
                )
            case 14:
                reset_text()
                reset_drop()
                self.cont.content = Column(
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
            whatsapp_icon.color = Colors.ON_SURFACE
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
    def data_binding(self):
        match tabs_widget.selected_index:
            case 0:
                self.qr.build_data(data_type="url", url=url_txt.value)
            case 1:
                self.qr.build_data(data_type="text", text=filled_txt.value)
            case 2:
                self.qr.build_data(data_type="mail", email=mail_txt.value, subject=subject_txt.value, msg=msg_txt.value)
            case 3:
                self.qr.build_data(data_type="phone", phone=phone_txt.value)
            case 4:
                self.qr.build_data(data_type="sms", phone=phone_txt.value, msg=msg_txt.value)
            case 5:
                self.qr.build_data(data_type="whatsapp", phone=phone_txt.value, msg=msg_txt.value)
            case 6:
                if vcard_ver_group.value == "3":
                    self.qr.build_data(data_type="vcard_v3", name=name_txt.value, lastname=lastname_txt.value,
                                       pos=pos_txt.value, org=org_txt.value, work_phone=work_phone_txt.value,
                                       priv_phone=priv_phone_txt.value, phone=phone_txt.value, email=mail_txt.value,
                                       url=url_txt.value, work_fax=work_fax_txt.value, priv_fax=priv_fax_txt.value, street=street_txt.value, birthday=self.birthday,
                                       zip=zip_txt.value, city=city_txt.value, state=state_txt.value,
                                       country=country_txt.value)
                else:
                    self.qr.build_data(data_type="vcard_v2", name=name_txt.value, lastname=lastname_txt.value,
                                       pos=pos_txt.value, org=org_txt.value, work_phone=work_phone_txt.value,
                                       priv_phone=priv_phone_txt.value, phone=phone_txt.value, email=mail_txt.value,
                                       url=url_txt.value, work_fax=work_fax_txt.value, priv_fax=priv_fax_txt.value, street=street_txt.value, birthday=self.birthday,
                                       zip=zip_txt.value, city=city_txt.value, state=state_txt.value,
                                       country=country_txt.value)
            case 7:
                self.qr.build_data(data_type="mecard", name=name_txt.value, lastname=lastname_txt.value, nick=nickname_txt.value, work_phone=work_phone_txt.value, priv_phone=priv_phone_txt.value, phone=phone_txt.value, email=mail_txt.value, url=url_txt.value, street=street_txt.value, birthday=self.birthday, zip=zip_txt.value, city=city_txt.value, state=state_txt.value, country=country_txt.value, note=filled_txt.value)
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

                self.qr.build_data(data_type="map", latitude=latitude_txt.value, longitude=longitude_txt.value)
            case 9:
                self.qr.build_data(data_type="wifi", ssid=ssid_txt.value, passwd=pass_txt.value, wifi_encrypt=wifi_encrypt_map.get(encrypt_drop.value, None), network_hide="true" if hidden_check.value else "false")
            case 10:
                self.qr.build_data(data_type="event", title=title_txt.value, location=location_txt.value, organizer=organizer_txt.value, summary=summary_txt.value, start_datetime=self.start_datetime, end_datetime=self.end_datetime)
            case 11:
                self.qr.build_data(data_type="app", app=app_txt.value)
            case 12:
                self.qr.build_data(data_type="favorite", title=title_txt.value, url=url_txt.value)
            case 13:
                self.qr.build_data(data_type="paypal", email=mail_txt.value, currency=currency_txt.value, price=price_txt.value, item_name=item_name_txt.value, thanks_url=thanks_url_txt.value, cancel_url=cancel_url_txt.value)
            case 14:
                self.qr.build_data(data_type="crypto", crypto_currency=crypto_currencies.get(crypto_drop.value, None), id=id_txt.value, amount=amount_txt.value, msg=msg_txt.value)


    def build_qr(self) -> str:
        self.data_binding()
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

        if self.qr.use_logo:
            correction_drop.value = "High"
            correction_drop.update()
            self.qr.error_correction = 2
        else:
            self.qr.error_correction = {"Low": 0, "Medium": 1, "High": 2, "Very High": 3}.get(correction_drop.value, None)

        if color_radio_group.value == "gradient":
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

    def remove_logo(self, e):
        if not self.delete_logo.disabled:
            self.qr.logo_path = ""
            self.qr.use_logo = False
            correction_drop.value = "Low"
            correction_drop.update()
            self.logo.src = "/placeholder.svg"
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

    def pick_image_result(self, e: FilePickerResultEvent):
        if e.files:  # Prevents Error if you cancel
            for file in e.files:
                print("Nombre del archivo:", file.name)
                print("Ruta del archivo:", file.path)
                print("Tamaño del archivo:", file.size)
            self.qr.colorMask_index = 5
            self.image.src = e.files[0].path
            self.qr.img_fill_path = e.files[0].path
            self.image.update()
            self.regenerate_preview(e)

    def save_file_result(self, e: FilePickerResultEvent):
        if e.path:  # Prevents save a filename named "None" in the app path
            self.qr.generate_final(e.path)
            print(f"Image saved in {e.path}")
            self.page.overlay.append(SnackBar(
                Text(f"Image saved in {e.path}"),
                True,
                bgcolor=Colors.GREEN,
            ))
            self.page.update()

    def build(self):
        return Column([
            Row([self.tabs_widget_container], alignment=MainAxisAlignment.CENTER), ResponsiveRow([self.main, self.right])
        ], expand=True, )

    def did_mount(self):
        self.page.overlay.extend([self.save_file_dialog, self.pick_files_dialog, self.pick_image_dialog])
        self.page.update()