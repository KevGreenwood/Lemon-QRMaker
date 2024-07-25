import flet as ft

def create_text_field(label, value=None, multiline=False, password=False, can_reveal_password=False, 
                        input_filter=None, filled=False, hint_text=None, width=None):
    return ft.TextField(
        value=value,
        multiline=multiline,
        password=password,
        can_reveal_password=can_reveal_password,
        input_filter=input_filter,
        label=label,
        filled=filled,
        hint_text=hint_text,
        width=width
    )

def input_filter(type: str):
    match type:
        case "phone":
            return ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string="")
        case "geo":
            return ft.InputFilter(allow=True, regex_string=r"[0-9-.]", replacement_string="")
        case "money":
            return ft.InputFilter(allow=True, regex_string=r"[0-9.]")

url_txt = create_text_field("Website URL", "https://")
url_txt.value = "https://github.com/KevGreenwood"
filled_txt = create_text_field("Write your text here", multiline=True, filled=True)
mail_txt = create_text_field("Email Address", hint_text="example@email.com")
subject_txt = create_text_field("Subject")
msg_txt = create_text_field("Message", multiline=True, filled=True)
phone_txt = create_text_field("Phone Number", input_filter=input_filter("phone"))
name_txt = create_text_field("First name", width=360)
lastname_txt = create_text_field("Last name", width=360)
org_txt = create_text_field("Organization", width=360)
pos_txt = create_text_field("Position (Work)", width=360)
work_phone_txt = create_text_field("Phone (Work)", input_filter=input_filter("phone"), width=360)
priv_phone_txt = create_text_field("Phone (Private)", input_filter=input_filter("phone"), width=360)
work_fax_txt = create_text_field("Fax (Work)", input_filter=input_filter("phone"), width=360)
priv_fax_txt = create_text_field("Fax (Private)", input_filter=input_filter("phone"), width=360)
street_txt = create_text_field("Street", multiline=True, width=360)
zip_txt = create_text_field("Zip code", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9+-]", replacement_string=""), width=360)
city_txt = create_text_field("City", width=360)
state_txt = create_text_field("State", width=360)
country_txt = create_text_field("Country", width=360)
nickname_txt = create_text_field("Nickname", width=360)
latitude_txt = create_text_field("Latitude", input_filter=input_filter("geo"), width=360)
longitude_txt = create_text_field("Longitude", input_filter=input_filter("geo"), width=360)
ssid_txt = create_text_field("Network Name", hint_text="SSID")
pass_txt = create_text_field("Password", password=True, can_reveal_password=True)
title_txt = create_text_field("Title")
location_txt = create_text_field("Event Location")
app_txt = create_text_field("App package name", hint_text="Example: com.google.android.youtube")
app_txt.helper_text="Search the Internet or use an app to find the package name."
crypto_address_txt = create_text_field("Receiver", hint_text="Bitcoin Address")
amount_txt = create_text_field("Amount", input_filter=input_filter("money"))
id_txt = create_text_field("ID")
item_name_txt = create_text_field("Item name", width=360)
item_id_txt = create_text_field("Item ID", width=360)
price_txt = create_text_field("Price", input_filter=input_filter("money"))
currency_txt = create_text_field("Currency", input_filter=ft.InputFilter(allow=True, regex_string=r"[a,...,z]"), width=360)
ship_txt = create_text_field("Shipping", input_filter=input_filter("money"), width=360)
tax_txt = create_text_field("Tax rate", input_filter=input_filter("money"), width=360)
border_txt = create_text_field("Ingrese el tamaño del borde", "4", input_filter=ft.NumbersOnlyInputFilter())
fore_color_txt = ft.TextField(
    label="Foreground Color",
    prefix_icon=ft.icons.COLOR_LENS,
    value="#000000"
)
back_color_txt = ft.TextField(
    label="Background Color",
    prefix_icon=ft.icons.COLOR_LENS,
    value="#FFFFFF"
)