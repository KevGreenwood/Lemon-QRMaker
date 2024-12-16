from datetime import datetime
from flet import (Text, ElevatedButton, Column, CupertinoDatePicker, ButtonStyle, RoundedRectangleBorder, CupertinoDatePickerMode, TextAlign)


start_dt_Text = Text(datetime.now().strftime("%Y/%m/%d %H:%M"), text_align=TextAlign.LEFT, size=20)
start_dt_Button = ElevatedButton(
    content=Column(
        [
            Text("Start Date", text_align=TextAlign.RIGHT, size=15),
            start_dt_Text
        ]
    ), style=ButtonStyle(shape=RoundedRectangleBorder()), width=360)

end_dt_Text = Text(datetime.now().strftime("%Y/%m/%d %H:%M"), text_align=TextAlign.LEFT, size=20)
end_dt_Button = ElevatedButton(
    content=Column(
        [
            Text("End Date", text_align=TextAlign.LEFT, size=15),
            end_dt_Text
        ]
    ), style=ButtonStyle(shape=RoundedRectangleBorder()), width=360)

start_dt_Picker = CupertinoDatePicker(date_picker_mode=CupertinoDatePickerMode.DATE_AND_TIME)
end_dt_Picker = CupertinoDatePicker(date_picker_mode=CupertinoDatePickerMode.DATE_AND_TIME)

birthday_Text = Text(datetime.now().strftime("%Y/%m/%d"), text_align=TextAlign.LEFT, size=20)
birthday_Button = ElevatedButton(
    content=Column(
        [
            Text("Birthday Date", text_align=TextAlign.LEFT, size=15),
            birthday_Text
        ]
    ), style=ButtonStyle(shape=RoundedRectangleBorder()),
width=360)