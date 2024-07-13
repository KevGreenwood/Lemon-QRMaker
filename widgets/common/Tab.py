import flet as ft

url_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.LINK), ft.Text("URL")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        text_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.TEXT_SNIPPET), ft.Text("Text")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        mail_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.MAIL), ft.Text("Email")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        phone_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PHONE), ft.Text("Phone")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        sms_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.SMS), ft.Text("SMS")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        wa_tab = ft.Tab(
            tab_content=ft.Column(
                [
                    ft.Image(
                        src="assets\\icons\\whatsapp.svg",
                        width=24,
                        height=24,
                        color=ft.colors.WHITE,
                    ),
                    ft.Text("Whatsapp"),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        vcard_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PERSON), ft.Text("VCard")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        mcard_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PERSON), ft.Text("MeCard")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        location_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.LOCATION_ON), ft.Text("Location")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        wifi_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.WIFI), ft.Text("WiFi")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        event_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.EVENT), ft.Text("Event")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        app_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.APPS), ft.Text("App")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        fav_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.BOOKMARK), ft.Text("Favorite")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        paypal_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.PAYPAL), ft.Text("PayPal")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        bitcoin_tab = ft.Tab(
            tab_content=ft.Column(
                [ft.Icon(ft.icons.CURRENCY_BITCOIN), ft.Text("Bitcoin")],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        tabs = ft.Tabs(
            tabs=[
                url_tab,
                text_tab,
                mail_tab,
                phone_tab,
                sms_tab,
                wa_tab,
                vcard_tab,
                mcard_tab,
                location_tab,
                wifi_tab,
                event_tab,
                app_tab,
                fav_tab,
                paypal_tab,
                bitcoin_tab,
            ],
            on_change=update,
            selected_index=0,
        )

        # Custom ft.Tab
        back = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=go_back,
            icon_color=ft.colors.WHITE,
            visible=False,
        )
        forward = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD_IOS,
            on_click=go_forward,
            icon_color=ft.colors.WHITE,
        )
        tab_row = ft.Row(
            controls=[
                back,
                ft.Column(controls=[tabs], expand=True),
                forward,
            ],
            width=750,
        )