from flet import *
from main import *


def main(page: Page):
    qr = QRGenerator()
    page.scroll = "always"

    def build_qr():
        qr.data = input_txt.value
        
        if ver_auto_box.value:
            qr.version = None
        else:
            qr.version = int(version_slider.value)
        
        qr.box_size = int(box_version_slider.value)

        if border_txt.value == "":
            qr.border = 0
        else:
            qr.border = int(border_txt.value)
        qr.back_color = back_color_txt.value
        qr.main_color = fore_color_txt.value
        qr.generate_preview()
        print(f"{qr.version}\n{qr.box_size}")
        return qr.preview

    def button_clicked(e):
        qr_preview.src_base64 = build_qr()
        page.update()



    input_txt = TextField(label="Ingrese el contenido", value="https://github.com/KevGreenwood", on_change=button_clicked)
    input_col = Column([input_txt])
    input_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("ENTER CONTENT")), expanded=True, content=input_col)])

    def switch_version(e):
        if ver_auto_box.value:
            version_slider.disabled = True
            version_slider.value = 1        
        else:
            version_slider.disabled = False
        qr_preview.src_base64 = build_qr()
        page.update()
    
    version_slider = Slider(min=1, max=40, divisions=39, label="{value}", value=1, disabled = True, on_change=button_clicked)
    ver_auto_box = Checkbox(label="Auto", value=True, on_change=switch_version)
    size_row = Row([version_slider, ver_auto_box])
    border_txt = TextField(label="Ingrese el tamaño del borde", value="4", on_change=button_clicked)
    size_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET SIZE")), content=Column([size_row, border_txt]))])
    
    color_radio_group = RadioGroup(content=Row([
        Radio(label="Single Color"),
        Radio(label="Color Gradient"),
        Checkbox(label="Custom Eye Color")
    ]))
    fore_color_txt = TextField(label="Foreground Color", prefix_icon=icons.COLOR_LENS, value="#000000", on_change=button_clicked)
    back_color_txt = TextField(label="Background Color", prefix_icon=icons.COLOR_LENS, value="#FFFFFF", on_change=button_clicked)
    fore_color_row = Row([fore_color_txt])
    color_column = Column([color_radio_group, fore_color_row, back_color_txt])
    color_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("SET COLORS")), content=color_column)])

    def pick_files_result(e: FilePickerResultEvent):
        for file in e.files:
            print("Nombre del archivo:", file.name)
            print("Ruta del archivo:", file.path)
            print("Tamaño del archivo:", file.size)
        logo.src = e.files[0].path
        logo.update()

    def get_logo_from_url(e):
        logo.src = url_logo.value
        logo.update()



    pick_files_dialog = FilePicker(on_result=pick_files_result)

    url_logo = TextField(on_change=get_logo_from_url)
    open_logo = ElevatedButton("Upload Logo", icon=icons.UPLOAD_FILE_ROUNDED, on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["png", "jpeg"]))
    logo = Image(src="default-preview-qr.svg", width=200, height=200)
    logo_preview = Container(logo)
    logo_column = Column([logo_preview, open_logo, url_logo])
    logo_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("ADD LOGO IMAGE")), content=logo_column)])

    body_shape = Row([
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_shape = Row([
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    eye_ball = Row([
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100),
        Image(src="default-preview-qr.svg", width=100, height=100)
        ])
    styles_col = Column([Text("Body Shape"), body_shape, Text("Eye Frame Shape"), eye_shape, Text("Eye Ball Shape"), eye_ball])
    design_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("CUSTOMIZE DESIGN")), content=styles_col)])
    
    error_dropdown = Dropdown(value="ERROR_CORRECT_M", options=[
        dropdown.Option("ERROR_CORRECT_L"),
        dropdown.Option("ERROR_CORRECT_M"),
        dropdown.Option("ERROR_CORRECT_Q"),
        dropdown.Option("ERROR_CORRECT_H"),
        ])
    error_panel = ExpansionPanelList([ExpansionPanel(header=ListTile(title=Text("ERROR CORRECTION")), content=error_dropdown)])
    
    qr_preview = Image(src="default-preview-qr.svg", width=300, height=300)
    conainer = Container(alignment=alignment.top_center, content=qr_preview)

    left_column = Column([input_panel, size_panel, color_panel, logo_panel, design_panel, error_panel])

    

    scale_txt = Text("1450 x 1450 px", color="black", weight=FontWeight.BOLD, text_align=TextAlign.CENTER)

    def update_scale_txt(e):
        slider_value = int(e.control.value)
        resolution = qr.get_res()
        scaled_resolution = tuple(i * slider_value for i in resolution)
        scale_txt.value = scaled_resolution
        scale_txt.update()


    box_version_slider = Slider(min=10, max=100, divisions=9, label="{value}", value=50, on_change=update_scale_txt)

    scale_column = Column(alignment=MainAxisAlignment.CENTER, controls=[box_version_slider, scale_txt])

    def save_file_result(e: FilePickerResultEvent):
        qr.generate(e.path)
        print(f"Image saved in {e.path}")

    save_file_dialog = FilePicker(on_result=save_file_result)

    save_btn = ElevatedButton("Save", icon=icons.SAVE_ALT_ROUNDED, on_click=lambda _: save_file_dialog.save_file(file_type=FilePickerFileType.IMAGE))

    buttons_row = Row(alignment=MainAxisAlignment.CENTER, controls=[ElevatedButton("Generate", on_click=button_clicked, icon=icons.QR_CODE_ROUNDED), save_btn])
    right_column = Column(alignment=alignment.top_center, controls=[conainer, scale_column, buttons_row])

    left = Container(alignment=alignment.top_left, bgcolor="#e8eef2", width=500, height=2000, col={"sm": 12, "md": 8, "xl": 8}, content=left_column)
    right = Container(bgcolor="white", width=300, height=2000, col={"sm": 12, "md": 4, "xl": 4}, content=right_column)
    main_container = ResponsiveRow(spacing=0, controls=[left, right])
    page.overlay.extend([pick_files_dialog, save_file_dialog])
    page.add(main_container)

app(target=main)