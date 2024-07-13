import flet as ft

url_txt = ft.TextField(
    value="https://github.com/KevGreenwood",
    label="Website URL",
    hint_text="https://"
)

filled_txt = ft.TextField(
    label="Write your text here",
    multiline=True,
    filled=True
)

mail_txt = ft.TextField(label="Email Address", hint_text="example@email.com")

subject_txt = ft.TextField(label="Subject")

msg_txt = ft.TextField(
    label="Message",    
    multiline=True,
    filled=True
)

phone_txt = ft.TextField(
    label="Phone Number",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string="")
)


name_txt = ft.TextField(label="First name", width=360)
lastname_txt = ft.TextField(label="Last name", width=360)
org_txt = ft.TextField(label="Organization", width=360)
pos_txt = ft.TextField(label="Position (Work)", width=360)

work_phone_txt = ft.TextField(
    label="Phone (Work)",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string=""),
    width=360
)

priv_phone_txt = ft.TextField(
    label="Phone (Private)",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string=""),
    width=360
)

work_fax_txt = ft.TextField(
    label="Fax (Work)",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string=""),
    width=360
)

priv_fax_txt = ft.TextField(
    label="Fax (Private)",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string=""),
    width=360
)

street_txt = ft.TextField(label="Street", multiline=True, width=360)

zip_txt = ft.TextField(
    label="Zip code",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+-]", replacement_string=""),
    width=360
)

city_txt = ft.TextField(label="City", width=360)
state_txt = ft.TextField(label="State", width=360)
country_txt = ft.TextField(label="Country", width=360)
nickname_txt = ft.TextField(label="Nickname", width=360)

latitude_txt = ft.TextField(
    label="Latitude",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9-.]", replacement_string=""),
    width=360
)

longitude_txt = ft.TextField(
    label="Longitude",
    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9-.]", replacement_string=""),
    width=360
)

ssid_txt = ft.TextField(label="Network Name", hint_text="SSID")