import flet as ft
from datetime import datetime


start_dt_Text = ft.Text(datetime.now().strftime("%Y/%m/%d %H:%M"), text_align=ft.TextAlign.LEFT, size=20)
start_dt_Button = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("Start Date", text_align=ft.TextAlign.RIGHT, size=15),
            start_dt_Text
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()), width=360)

end_dt_Text = ft.Text(datetime.now().strftime("%Y/%m/%d %H:%M"), text_align=ft.TextAlign.LEFT, size=20)
end_dt_Button = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("End Date", text_align=ft.TextAlign.LEFT, size=15),
            end_dt_Text
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()), width=360)

start_dt_Picker = ft.CupertinoDatePicker(date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME)
end_dt_Picker = ft.CupertinoDatePicker(date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME)

birthday_Text = ft.Text(datetime.now().strftime("%Y/%m/%d"), text_align=ft.TextAlign.LEFT, size=20)
birthday_Button = ft.ElevatedButton(
    content=ft.Column(
        [
            ft.Text("Birthday Date", text_align=ft.TextAlign.LEFT, size=15),
            birthday_Text
        ]
    ), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder()),
width=360)