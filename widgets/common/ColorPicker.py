import flet as ft
from flet_contrib.color_picker import ColorPicker
from utils.color_coverter import hex_to_rgb


class ColorButtonPicker(ft.ElevatedButton):
    def __init__(self, text, icon, color, **kwargs):
        super().__init__(text, icon, icon_color=color, on_click=self.open_color_picker, **kwargs)
        self.start_color = color
        self.qr_color: tuple = hex_to_rgb(color)
        self.fx = None
        self.color_Picker = ColorPicker(color, 300)
        self.confirm_text = ft.TextButton("OK", on_click=self.change_color)
        self.color_dialog = ft.AlertDialog(
                content=self.color_Picker,
                actions=[
                    self.confirm_text,
                    ft.TextButton("Cancel", on_click=self.close_dialog),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
    
    def open_color_picker(self, e):
        e.page.overlay.append(self.color_dialog)
        self.color_dialog.open = True
        e.page.update()
    
    def change_color(self, e):
        self.icon_color = self.color_Picker.color
        self.qr_color = hex_to_rgb(self.color_Picker.color)
        self.fx(e)
        self.color_dialog.open = False
        e.page.update()

    def close_dialog(self, e):
        self.color_Picker.color = self.start_color
        self.qr_color = hex_to_rgb(self.color_Picker.color)
        self.color_dialog.open = False
        e.page.update()

background_Button = ColorButtonPicker("Background Color", ft.Icons.SQUARE, "#FFFFFF")
foreground_Button = ColorButtonPicker("Foreground Color", ft.Icons.SQUARE, "#000000")
gradient_Button = ColorButtonPicker("Gradient Color", ft.Icons.SQUARE, "#0000FF")

inner_eye_Button = ColorButtonPicker("Inner Eye Color", ft.Icons.SQUARE, "#000000")
inner_eye_gradient_Button = ColorButtonPicker("Inner Eye Gradient Color", ft.Icons.SQUARE, "#0000FF")

outer_eye_Button = ColorButtonPicker("Outer Eye Color", ft.Icons.SQUARE, "#000000")
outer_eye_gradient_Button = ColorButtonPicker("Outer Eye Gradient Color", ft.Icons.SQUARE, "#0000FF")