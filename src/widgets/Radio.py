from flet import (Row, Radio, RadioGroup)


color_radio_group = RadioGroup(Row(
                [
                    Radio("Single Color", value="normal"),
                    Radio("Color Gradient", value="gradient"),
                    Radio("Image Fill", value="image")
                ]
            ), "normal"
        )

vcard_ver_group = RadioGroup(Row(
        [
            Radio("Version 2.1", value="2.1"),
            Radio("Version 3", value="3")
        ]
    ), "3"
)