import flet as ft

def main(page: ft.Page):
    page.scroll = "always"
    
    input_txt = ft.TextField(label="Ingrese el contenido", value="https://github.com/KevGreenwood")
    type_dropdown = ft.Dropdown(options=[
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

    color_radio_group = ft.RadioGroup(content=ft.Row([
        ft.Radio(label="Single Color"),
        ft.Radio(label="Color Gradient"),
        ft.Checkbox(label="Custome Eye Color")
    ]))

    fore_color_txt = ft.TextField(label="Foreground Color", value="#000000")
    back_color_txt = ft.TextField(label="Background Color", value="#FFFFFF")

    fore_color_row = ft.Row([fore_color_txt])

    color_column = ft.Column([color_radio_group, fore_color_row, back_color_txt])


    color_panel = ft.ExpansionPanelList([ft.ExpansionPanel(header=ft.ListTile(title=ft.Text("SET COLORS")), content=color_column)])

    logo_preview = ft.Container(content=ft.Image(src="default-preview-qr.svg", width=200, height=200))
    logo_column = ft.Column([logo_preview, ft.ElevatedButton("Upload Logo")])

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

    left_column = ft.Column(controls=[input_panel, color_panel, logo_panel, design_panel])


    qr_preview = ft.Container(alignment=ft.alignment.top_center, content=ft.Image(src="default-preview-qr.svg", width=300, height=300))
    size_slider = ft.Slider(min=1, max=40, divisions=40)
    size_txt = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text("Low Quality"), ft.Text("Size"),ft.Text("High Quality")])
    buttons_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.ElevatedButton("Generate"), ft.ElevatedButton("Save")])
    right_column = ft.Column(alignment=ft.alignment.top_center, controls=[qr_preview, size_slider, size_txt, buttons_row])

    left = ft.Container(alignment=ft.alignment.top_left, bgcolor="#e8eef2", width=500, height=1000, col={"sm": 12, "md": 8, "xl": 8}, content=left_column)
    right = ft.Container(bgcolor="white", width=300, height=1000, col={"sm": 12, "md": 4, "xl": 4}, content=right_column)
    main_container = ft.ResponsiveRow(spacing=0, controls=[left, right])

    page.add(main_container)

ft.app(target=main)