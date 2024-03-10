import flet as ft
from main import *


def main(page: ft.Page):
    page.scroll = "always"

    input_txt = ft.TextField(label="Ingrese el contenido", value="https://github.com/KevGreenwood")
    type_dropdown = ft.Dropdown(value="General", options=[
        ft.dropdown.Option("General"),
        ft.dropdown.Option("Email"),
        ft.dropdown.Option("SMS"),
        ft.dropdown.Option("VCard"),
        ft.dropdown.Option("Mecard"),
        ft.dropdown.Option("Event"),
        ft.dropdown.Option("WiFi"),
        ft.dropdown.Option("Mecard")
        ])
    input_col = ft.Column([type_dropdown, input_txt])
    input_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("ENTER CONTENT")), expanded=True, content=input_col)])

    size_slider = ft.Slider(min=1, max=40, divisions=39, label="{value}")
    size_row = ft.Row([size_slider, ft.Checkbox(label="Auto", value=True)])
    border_txt = ft.TextField(label="Ingrese el tamaño del borde", value="4")
    size_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("SET SIZE")), content=ft.Column([size_row, border_txt]))])
    

    color_radio_group = ft.RadioGroup(content=ft.Row([
        ft.Radio(label="Single Color"),
        ft.Radio(label="Color Gradient"),
        ft.Checkbox(label="Custome Eye Color")
    ]))
    fore_color_txt = ft.TextField(label="Foreground Color", prefix_icon=ft.icons.COLOR_LENS, value="#000000")
    back_color_txt = ft.TextField(label="Background Color", prefix_icon=ft.icons.COLOR_LENS, value="#FFFFFF")
    fore_color_row = ft.Row([fore_color_txt])
    color_column = ft.Column([color_radio_group, fore_color_row, back_color_txt])
    color_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("SET COLORS")), content=color_column)])

    logo_preview = ft.Container(content=ft.Image(src="default-preview-qr.svg", width=200, height=200))
    logo_column = ft.Column([logo_preview, ft.ElevatedButton("Upload Logo", icon=ft.icons.UPLOAD_FILE_ROUNDED)])
    logo_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("ADD LOGO IMAGE")), content=logo_column)])

    body_shape = ft.Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_shape = ft.Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_ball = ft.Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    styles_col = ft.Column([ft.Text("Body Shape"), body_shape, ft.Text("Eye Frame Shape"), eye_shape, ft.Text("Eye Ball Shape"), eye_ball])
    design_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("CUSTOMIZE DESIGN")), content=styles_col)])
    
    error_dropdown = ft.Dropdown(value="ERROR_CORRECT_M", options=[
        ft.dropdown.Option("ERROR_CORRECT_L"),
        ft.dropdown.Option("ERROR_CORRECT_M"),
        ft.dropdown.Option("ERROR_CORRECT_Q"),
        ft.dropdown.Option("ERROR_CORRECT_H"),
        ])
    error_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("ERROR CORRECTION")), content=error_dropdown)])
    left_column = ft.Column([input_panel, size_panel, color_panel, logo_panel, design_panel, error_panel])

    qr_preview = ft.Image(src="default-preview-qr.svg", width=300, height=300)
    conainer = ft.Container(alignment=ft.alignment.top_center, content=qr_preview)

    def build_qr():
        qr = QRGenerator()
        qr.data = input_txt.value
        qr.version = size_slider.value
        qr.box_size = box_size_slider.value
        qr.border = int(border_txt.value)
        qr.back_color = back_color_txt.value
        qr.main_color = fore_color_txt.value
        qr.generate()
        return qr.preview

    def button_clicked(e):
        qr_preview.src_base64 = build_qr()
        page.update()

    scale_txt = ft.Text("1450 x 1450 px", color="black", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    def update_scale_txt(e):
        slider_value = int(e.control.value)
        scale_txt.value = f"{29*slider_value} x {29*slider_value} px"
        page.update()

    box_size_slider = ft.Slider(min=10, max=100, divisions=9, label="{value}", value=50, on_change=update_scale_txt)

    scale_column = ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[box_size_slider, scale_txt])
    buttons_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.ElevatedButton("Generate", on_click=button_clicked, icon=ft.icons.QR_CODE_ROUNDED), ft.ElevatedButton("Save", icon=ft.icons.SAVE_ALT_ROUNDED)])
    right_column = ft.Column(alignment=ft.alignment.top_center, controls=[conainer, scale_column, buttons_row])

    left = ft.Container(alignment=ft.alignment.top_left, bgcolor="#e8eef2", width=500, height=2000, col={"sm": 12, "md": 8, "xl": 8}, content=left_column)
    right = ft.Container(bgcolor="white", width=300, height=2000, col={"sm": 12, "md": 4, "xl": 4}, content=right_column)
    main_container = ft.ResponsiveRow(spacing=0, controls=[left, right])

    page.add(main_container)

ft.app(target=main)