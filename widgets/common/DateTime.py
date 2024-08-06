import flet as ft
from datetime import datetime


current_start_date = ft.Text(datetime.now().strftime("%d/%m/%Y %H:%M"), text_align=ft.TextAlign.LEFT, size=20)
start_date = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("Start Date", text_align=ft.TextAlign.LEFT, size=15),
            current_start_date
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()))

current_end_date = ft.Text(datetime.now().strftime("%d/%m/%Y %H:%M"), text_align=ft.TextAlign.LEFT, size=20)
end_date = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("End Date", text_align=ft.TextAlign.LEFT, size=15),
            current_end_date
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()))

