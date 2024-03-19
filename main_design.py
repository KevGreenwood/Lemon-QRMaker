from flet import *
import flet as ft
from main import *


def main(page: Page):
    page.title = "Cassie-QRCodeMaker"
    page.scroll = "always"
    
    # --- QR Building ---
    qr = QRGenerator()
    def build_qr():
        qr.data = input_txt.value
        if ver_auto_box.value:
            qr.version = None
        else:
            qr.version = int(version_slider.value)
        qr.box_size = int(qr_size_slider.value)
        if border_txt.value == "":
            qr.border = 4
        else:
            qr.border = int(border_txt.value)
        qr.back_color = back_color_txt.value
        qr.main_color = fore_color_txt.value

        print(f"Version: {qr.version}\nSize: {qr.box_size}")

        return qr.generate_preview()

    # --- Realtime Building ---
    def regenerate_preview(e):
        qr_preview.src_base64 = build_qr()
        qr_preview.update()

    def switch_version(e):
        if ver_auto_box.value:
            version_slider.disabled = True
            version_slider.value = 1        
        else:
            version_slider.disabled = False
        version_slider.update()
        regenerate_preview(e)

    # --- Input Section ---
    input_txt = TextField(label="Ingrese el contenido", value="https://github.com/KevGreenwood", on_change=regenerate_preview)
    input_col = Column([input_txt])
    input_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("ENTER CONTENT")), expanded=True, content=input_col)])

    # --- Size Section ---
    version_slider = Slider(min=1, max=40, divisions=39, label="{value}", value=1, disabled = True, on_change=regenerate_preview)
    ver_auto_box = Checkbox(label="Auto", value=True, on_change=switch_version)
    size_row = Row([version_slider, ver_auto_box])
    border_txt = TextField(label="Ingrese el tamaño del borde", value="4", input_filter=NumbersOnlyInputFilter(),on_change=regenerate_preview)
    size_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET SIZE")), content=Column([size_row, border_txt]))])
    
    # --- Color Section ---
    color_radio_group = RadioGroup(content=Row([
        Radio(label="Single Color"),
        Radio(label="Color Gradient"),
        Checkbox(label="Custom Eye Color")
    ]))
    fore_color_txt = TextField(label="Foreground Color", prefix_icon=icons.COLOR_LENS, value="#000000", on_change=regenerate_preview)
    back_color_txt = TextField(label="Background Color", prefix_icon=icons.COLOR_LENS, value="#FFFFFF", on_change=regenerate_preview)
    fore_color_row = Row([fore_color_txt])
    color_column = Column([color_radio_group, fore_color_row, back_color_txt])
    color_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET COLORS")), content=color_column)])
    
    def pick_files_result(e: FilePickerResultEvent):
        for file in e.files:
            print("Nombre del archivo:", file.name)
            print("Ruta del archivo:", file.path)
            print("Tamaño del archivo:", file.size)
        logo.src = e.files[0].path
        qr.logo_path = e.files[0].path
        qr.use_logo = True
        logo.update()
        regenerate_preview(e)
    pick_files_dialog = FilePicker(on_result=pick_files_result)

    def remove_logo(e):
        qr.logo_path = None
        qr.use_logo = False
        logo.update()
        regenerate_preview(e)

    open_logo = ElevatedButton("Upload Logo", icon=icons.UPLOAD_FILE_ROUNDED, on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg"]))
    delete_logo = ElevatedButton("Delete Logo", icon=icons.REMOVE_CIRCLE_OUTLINE_ROUNDED, on_click=remove_logo)
    logo = ft.Image(src="default-preview-qr.svg", width=200, height=200)
    logo_preview = Container(logo)
    logo_column = Column([logo_preview, open_logo, delete_logo])
    logo_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("ADD LOGO IMAGE")), content=logo_column)])

    body_shape = Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_shape = Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_ball = Row([
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100),
        ft.Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    styles_col = Column([Text("Body Shape"), body_shape, Text("Eye Frame Shape"), eye_shape, Text("Eye Ball Shape"), eye_ball])
    design_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("CUSTOMIZE DESIGN")), content=styles_col)])

    left_column = Column([input_panel, size_panel, color_panel, logo_panel, design_panel])


    def update_scale_txt(e):
        regenerate_preview(e)
        scale_txt.value = qr.get_res()
        scale_txt.update()

    qr_size_slider = Slider(min=10, max=100, divisions=9, label="{value}", value=50, on_change=update_scale_txt)
    qr_preview = ft.Image(src_base64=build_qr(),width=300, height=300)

    scale_txt = Text(value=qr.get_res(), color="black", weight=FontWeight.BOLD)


    prev_container = Container(alignment=alignment.top_center, content=qr_preview)
    scale_column = Column(alignment=MainAxisAlignment.CENTER, controls=[qr_size_slider, scale_txt])

    def save_file_result(e: FilePickerResultEvent):
        qr.generate_final(e.path)
        print(f"Image saved in {e.path}")

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_btn = ElevatedButton("Save", icon=icons.SAVE_ALT_ROUNDED, on_click=lambda _: save_file_dialog.save_file(file_type=FilePickerFileType.IMAGE))

    buttons_row = Row(alignment=MainAxisAlignment.CENTER, controls=[save_btn, ])
    right_column = Column(alignment=alignment.top_center, controls=[prev_container, scale_column, buttons_row])

    left = Container(alignment=alignment.top_left, bgcolor="#e8eef2", width=500, height=2000, col={"sm": 12, "md": 8, "xl": 8}, content=left_column)
    right = Container(bgcolor="white", width=300, height=2000, col={"sm": 12, "md": 4, "xl": 4}, content=right_column)
    main_container = ResponsiveRow(spacing=0, controls=[left, right])

    page.overlay.extend([pick_files_dialog, save_file_dialog])
    page.add(main_container)

app(target=main)