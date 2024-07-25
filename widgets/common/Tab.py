import flet as ft

def create_tab(icon: ft.icons, text: str):
    return ft.Tab(
        tab_content=ft.Column(
            controls=[ft.Icon(icon), ft.Text(text)],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    )

whatsapp_icon = ft.Image(
    src="assets\\icons\\whatsapp.svg",
    width=24,
    height=24,
    color=ft.colors.ON_BACKGROUND
)

tabs = [
    create_tab(ft.icons.LINK, "URL"),
    create_tab(ft.icons.TEXT_SNIPPET, "Text"),
    create_tab(ft.icons.MAIL, "Email"),
    create_tab(ft.icons.PHONE, "Phone"),
    create_tab(ft.icons.SMS, "SMS"),
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
    create_tab(ft.icons.PERSON, "VCard"),
    create_tab(ft.icons.PERSON, "MeCard"),
    create_tab(ft.icons.LOCATION_ON, "Location"),
    create_tab(ft.icons.WIFI, "WiFi"),
    create_tab(ft.icons.EVENT, "Event"),
    create_tab(ft.icons.APPS, "App"),
    create_tab(ft.icons.BOOKMARK, "Favorite"),
    create_tab(ft.icons.PAYPAL, "PayPal"),
    create_tab(ft.icons.CURRENCY_BITCOIN, "Bitcoin")
]

tabs_widget = ft.Tabs(
    tabs=tabs,
    selected_index=0
)

# Custom ft.Tab
back = ft.IconButton(
    icon=ft.icons.ARROW_BACK_IOS,
    icon_color=ft.colors.WHITE,
    visible=False
)

forward = ft.IconButton(
    icon=ft.icons.ARROW_FORWARD_IOS,
    icon_color=ft.colors.WHITE
)

tab_row = ft.Row(
    controls=[
        back,
        ft.Column(controls=[tabs_widget], expand=True),
        forward
    ],
    width=750
)