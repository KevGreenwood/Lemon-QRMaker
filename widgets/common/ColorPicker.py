import flet as ft
from flet_contrib.color_picker import ColorPicker


import flet as ft

class ColorButtonPicker(ft.ElevatedButton):
    def __init__(self, text, icon, color,**kwargs):
        super().__init__(text, icon, icon_color=color, on_click=self.open_color_picker, **kwargs)
        
        self.start_color = color
        
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
    
    def hex_to_rgb(self, hex_value):
        hex_value = hex_value.lstrip("#")
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def open_color_picker(self, e):
        e.page.overlay.append(self.color_dialog)
        self.color_dialog.open = True
        e.page.update()

    def close_dialog(self, e):
        self.color_dialog.open = False
        self.color_Picker.color = self.start_color
        e.page.update()

    def change_color(self, e):
        self.icon_color = self.color_Picker.color
        print(self.hex_to_rgb(self.icon_color))
        self.color_dialog.open = False
        self.fx(e)
        e.page.update()

background_Button = ColorButtonPicker("Background Color", ft.icons.SQUARE, "#FFFFFF")
foreground_Button = ColorButtonPicker("Foreground Color", ft.icons.SQUARE, "#000000")
gradient_Button = ColorButtonPicker("sI", ft.icons.SQUARE, "#0000FF")