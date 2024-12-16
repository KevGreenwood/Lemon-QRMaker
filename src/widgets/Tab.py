from flet import (Tab, Column, Text, Icon, Image, Colors, IconButton, Row, Tabs, Icons, CrossAxisAlignment)


def create_tab(icon: Icons, text: str):
    return Tab(
        tab_content=Column(
            [Icon(icon), Text(text)],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0
        )
    )

whatsapp_icon = Image(
    src="/icons/whatsapp.svg",
    width=24,
    height=24,
    color=Colors.ON_SURFACE
)

tabs = [
    create_tab(Icons.LINK, "URL"),
    create_tab(Icons.TEXT_SNIPPET, "Text"),
    create_tab(Icons.MAIL, "Email"),
    create_tab(Icons.PHONE, "Phone"),
    create_tab(Icons.SMS, "SMS"),
    Tab(
        tab_content=Column(
            [
                whatsapp_icon,
                Text("Whatsapp"),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0
        )
    ),
    create_tab(Icons.PERSON, "VCard"),
    create_tab(Icons.PERSON, "MeCard"),
    create_tab(Icons.LOCATION_ON, "Location"),
    create_tab(Icons.WIFI, "WiFi"),
    create_tab(Icons.EVENT, "Event"),
    create_tab(Icons.APPS, "App"),
    create_tab(Icons.BOOKMARK, "Favorite"),
    create_tab(Icons.PAYPAL, "PayPal"),
    create_tab(Icons.CURRENCY_BITCOIN, "Bitcoin")
]

tabs_widget = Tabs(tabs, 0)

# Custom Tab
back = IconButton(
    Icons.ARROW_BACK_IOS,
    Colors.WHITE,
    disabled=True
)

forward = IconButton(Icons.ARROW_FORWARD_IOS, Colors.WHITE)

tab_row = Row(
    [
        back,
        Column(controls=[tabs_widget], expand=True),
        forward
    ],
    width=750
)