import flet as ft


class CustomTextField(ft.TextField):
    def __init__(self, label, value=None, multiline=False, password=False,
                can_reveal_password=False, input_filter=None, filled=False,
                hint_text=None, prefix_text=None, suffix_text=None, width=None):
        super().__init__()
        self.value = value
        self.multiline = multiline
        self.password = password
        self.can_reveal_password = can_reveal_password
        self.input_filter = self.get_input_filter(input_filter)
        self.label = label
        self.filled = filled
        self.hint_text = hint_text
        self.prefix_text = prefix_text
        self.suffix_text = suffix_text
        self.width = width
    
    def get_input_filter(self, filter_type):
        filters = {
            "num": ft.NumbersOnlyInputFilter(),
            "phone": ft.InputFilter(allow=True, regex_string=r"[0-9+]", replacement_string=""),
            "geo": ft.InputFilter(allow=True, regex_string=r"[0-9-.]", replacement_string=""),
            "zip": ft.InputFilter(allow=True, regex_string=r"[0-9-]", replacement_string=""),
            "money": ft.InputFilter(allow=True, regex_string=r"[0-9.]"),
            "currency": ft.TextOnlyInputFilter()
        }
        return filters.get(filter_type) 

url_txt = CustomTextField("Website URL", "https://github.com/KevGreenwood", hint_text="https://")
filled_txt = CustomTextField("Write your text here", multiline=True, filled=True)
mail_txt = CustomTextField("Email Address", hint_text="example@email.com")
subject_txt = CustomTextField("Subject")
msg_txt = CustomTextField("Message", multiline=True, filled=True)
phone_txt = CustomTextField("Phone Number", input_filter="phone")
name_txt = CustomTextField("First name", width=360)
lastname_txt = CustomTextField("Last name", width=360)
org_txt = CustomTextField("Organization", width=360)
pos_txt = CustomTextField("Position (Work)", width=360)
work_phone_txt = CustomTextField("Phone (Work)", input_filter="phone", width=360)
priv_phone_txt = CustomTextField("Phone (Private)", input_filter="phone", width=360)
work_fax_txt = CustomTextField("Fax (Work)", input_filter="phone", width=360)
priv_fax_txt = CustomTextField("Fax (Private)", input_filter="phone", width=360)
street_txt = CustomTextField("Street", multiline=True, width=360)
zip_txt = CustomTextField("Zip code", input_filter="zip", width=360)
city_txt = CustomTextField("City", width=360)
state_txt = CustomTextField("State", width=360)
country_txt = CustomTextField("Country", width=360)
nickname_txt = CustomTextField("Nickname", width=360)
latitude_txt = CustomTextField("Latitude", input_filter="geo", width=360)
longitude_txt = CustomTextField("Longitude", input_filter="geo", width=360)
ssid_txt = CustomTextField("Network Name", hint_text="SSID")
pass_txt = CustomTextField("Password", password=True, can_reveal_password=True)
title_txt = CustomTextField("Title")
location_txt = CustomTextField("Event Location")
organizer_txt = CustomTextField("Organizer")
summary_txt = CustomTextField("Summary")
app_txt = CustomTextField("App package name", hint_text="Example: com.google.android.youtube")
app_txt.helper_text="Search the Internet or use an app to find the package name."
crypto_address_txt = CustomTextField("Receiver", hint_text="Bitcoin Address")
amount_txt = CustomTextField("Amount", input_filter="money", prefix_text="$")
id_txt = CustomTextField("ID")
item_name_txt = CustomTextField("Item name", width=360)
item_id_txt = CustomTextField("Item ID", width=360)
price_txt = CustomTextField("Price", input_filter="money", prefix_text="$", width=360)
currency_txt = CustomTextField("Currency Code", input_filter="currency", hint_text="USD", width=360)
ship_txt = CustomTextField("Shipping", input_filter="money", prefix_text="$", width=360)
tax_txt = CustomTextField("Tax rate", input_filter="money", suffix_text="%", width=360)
border_txt = CustomTextField("Ingrese el tamaño del borde", "4", input_filter="num")
thanks_url_txt = CustomTextField("Thank you URL", hint_text="https://", width=360)
cancel_url_txt = CustomTextField("Cancel URL", hint_text="https://", width=360)


def reset_text(placeholder: bool = False):
    if placeholder:
        url_txt.value = "https://github.com/KevGreenwood"
    else:
        url_txt.value = None
    filled_txt.value = None
    mail_txt.value = None
    subject_txt.value = None
    msg_txt.value = None
    phone_txt.value = None
    name_txt.value = None
    lastname_txt.value = None
    org_txt.value = None
    pos_txt.value = None
    work_phone_txt.value = None
    priv_phone_txt.value = None
    work_fax_txt.value = None
    priv_fax_txt.value = None
    street_txt.value = None
    zip_txt.value = None
    city_txt.value = None
    state_txt.value = None
    country_txt.value = None
    nickname_txt.value = None
    latitude_txt.value = None
    longitude_txt.value = None
    ssid_txt.value = None
    pass_txt.value = None
    title_txt.value = None
    location_txt.value = None
    app_txt.value = None
    crypto_address_txt.value = None
    amount_txt.value = None
    id_txt.value = None
    item_name_txt.value = None
    item_id_txt.value = None
    price_txt.value = None
    currency_txt.value = None
    ship_txt.value = None
    tax_txt.value = None
    
def card_pages():
    reset_text()
    phone_txt.width = 360
    mail_txt.width = 360
    url_txt.width = 360