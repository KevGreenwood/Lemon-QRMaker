import flet as ft

def create_tab(icon: ft.Icons, text: str):
    return ft.Tab(
        tab_content=ft.Column(
            [ft.Icon(icon), ft.Text(text)],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    )

whatsapp_icon = ft.Image(
    src="assets\\icons\\whatsapp.svg",
    width=24,
    height=24,
    color=ft.Colors.ON_SURFACE
)

tabs = [
    create_tab(ft.Icons.LINK, "URL"),
    create_tab(ft.Icons.TEXT_SNIPPET, "Text"),
    create_tab(ft.Icons.MAIL, "Email"),
    create_tab(ft.Icons.PHONE, "Phone"),
    create_tab(ft.Icons.SMS, "SMS"),
    ft.Tab(
        tab_content=ft.Column(
            [
                whatsapp_icon,
                ft.Text("Whatsapp"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    ),
    create_tab(ft.Icons.PERSON, "VCard"),
    create_tab(ft.Icons.PERSON, "MeCard"),
    create_tab(ft.Icons.LOCATION_ON, "Location"),
    create_tab(ft.Icons.WIFI, "WiFi"),
    create_tab(ft.Icons.EVENT, "Event"),
    create_tab(ft.Icons.APPS, "App"),
    create_tab(ft.Icons.BOOKMARK, "Favorite"),
    create_tab(ft.Icons.PAYPAL, "PayPal"),
    create_tab(ft.Icons.CURRENCY_BITCOIN, "Bitcoin")
]

tabs_widget = ft.Tabs(tabs, 0)

# Custom ft.Tab
back = ft.IconButton(
    ft.Icons.ARROW_BACK_IOS,
    ft.Colors.WHITE,
    disabled=True
)

forward = ft.IconButton(ft.Icons.ARROW_FORWARD_IOS, ft.Colors.WHITE)

tab_row = ft.Row(
    [
        back,
        ft.Column(controls=[tabs_widget], expand=True),
        forward
    ],
    width=750
)