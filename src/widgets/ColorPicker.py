from flet import (ElevatedButton, TextButton, AlertDialog, Icons, MainAxisAlignment)
from flet_contrib.color_picker import ColorPicker


def hex_to_rgb(color: str):
    color = color.lstrip("#")
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

class ColorButtonPicker(ElevatedButton):
    def __init__(self, text, icon, color):
        super().__init__(text, icon, icon_color=color, on_click=self.open_color_picker)
        self.start_color = color
        self.qr_color: tuple = hex_to_rgb(color)
        self.color_Picker = ColorPicker(color, 300)
        self.confirm_text = TextButton("OK", on_click=self.change_color)
        self.color_dialog = AlertDialog(
                content=self.color_Picker,
                actions=[
                    self.confirm_text,
                    TextButton("Cancel", on_click=self.close_dialog),
                ],
                actions_alignment=MainAxisAlignment.END,
            )
    
    def open_color_picker(self, e):
        e.page.overlay.append(self.color_dialog)
        self.color_dialog.open = True
        e.page.update()
    
    def change_color(self, e):
        self.icon_color = self.color_Picker.color
        self.qr_color = hex_to_rgb(self.color_Picker.color)
        self.color_dialog.open = False
        e.page.update()

    def close_dialog(self, e):
        self.color_Picker.color = self.start_color
        self.qr_color = hex_to_rgb(self.color_Picker.color)
        self.color_dialog.open = False
        e.page.update()

background_Button = ColorButtonPicker("Background Color", Icons.SQUARE, "#FFFFFF")
foreground_Button = ColorButtonPicker("Foreground Color", Icons.SQUARE, "#000000")
gradient_Button = ColorButtonPicker("Gradient Color", Icons.SQUARE, "#0000FF")

"""
inner_eye_Button = ColorButtonPicker("Inner Eye Color", Icons.SQUARE, "#000000")
inner_eye_gradient_Button = ColorButtonPicker("Inner Eye Gradient Color", Icons.SQUARE, "#0000FF")

outer_eye_Button = ColorButtonPicker("Outer Eye Color", Icons.SQUARE, "#000000")
outer_eye_gradient_Button = ColorButtonPicker("Outer Eye Gradient Color", Icons.SQUARE, "#0000FF")
"""