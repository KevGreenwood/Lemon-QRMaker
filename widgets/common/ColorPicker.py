import flet as ft
from flet_contrib.color_picker import ColorPicker

class ColorPickerButton(ft.ElevatedButton):
    def __init_(self, text, icon, icon_colorm, on_click):
        super().__init__()
        self.text


def open_color_picker(e):
    e.page.overlay.append(d)
    d.open = True
    e.page.update()



def close_dialog(e):
    d.open = False
    e.update()



def change_color(e, fx):
    background_Button.icon_color = background_Picker.color
    d.open = False
    fx(e)
    e.page.update()









background_Picker = ColorPicker(color="#000000", width=300)
background_Button = ft.ElevatedButton("Background Color", ft.icons.SQUARE, on_click=open_color_picker)

foreground_Picker = ColorPicker(color="#FFFFFF", width=300)
foreground_Button = ft.ElevatedButton("Foreground Color", ft.icons.SQUARE,)

gradient_Picker = ColorPicker(color="#0000FF", width=300)
gradient_Button = ft.ElevatedButton(icon=ft.icons.SQUARE,)

confirm_text = ft.TextButton("OK")



def generate_dialog():
    return ft.AlertDialog(
        content=background_Picker,
        actions=[
            confirm_text,
            ft.TextButton("Cancel", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


d = 