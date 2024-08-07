import flet as ft
from datetime import datetime

current_start_date = datetime.now().strftime("%Y/%m/%d %H:%M")
current_end_date = datetime.now().strftime("%Y/%m/%d %H:%M")

current_start_date_Text = ft.Text(current_start_date, text_align=ft.TextAlign.LEFT, size=20)
start_date = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("Start Date", text_align=ft.TextAlign.RIGHT, size=15),
            current_start_date_Text
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()))

current_end_date_Text = ft.Text(current_end_date, text_align=ft.TextAlign.LEFT, size=20)
end_date = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("End Date", text_align=ft.TextAlign.LEFT, size=15),
            current_end_date_Text
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()))

start_date_picker = ft.CupertinoDatePicker(date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME)
end_date_picker = ft.CupertinoDatePicker(date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME)

def format(type):
    if type == 0:
        x = None
        x = datetime.strptime(current_start_date, "%Y/%m/%d %H:%M")
        return x.strftime("%Y%m%dT%H%M")
    else:
        x = None
        x = datetime.strptime(current_end_date, "%Y/%m/%d %H:%M")
        return x.strftime("%Y%m%dT%H%M")