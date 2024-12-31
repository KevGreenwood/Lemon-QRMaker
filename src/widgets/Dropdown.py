from flet import (Dropdown, dropdown)


crypto_currencies = {
                    "Bitcoin": "bitcoin",
                    "Bitcoin Cash": "bitcoincash",
                    "Ethereum": "ethereum",
                    "Litecoin": "litecoin",
                    "Dash": "dash",
                }

wifi_encrypt_map = {"None": "nopass", "WEP": "WEP", "WPA/WPA2": "WPA"}

gradiant_style_map = {"Radial Gradient": 1, "Square Gradient": 2, "Horizontal Gradient": 3, "Vertical Gradient": 4}

class CustomDropdown(Dropdown):
    def __init__(self, value, options, label, width=None):
        super().__init__()
        self.value=value
        self.options=[dropdown.Option(option) for option in options]
        self.label=label
        self.width=width

def reset_drop():
    vcard_ver.value = "Version 3"
    encrypt_drop.value = "WPA/WPA2"
    crypto_drop.value = "Bitcoin"
    payment_drop.value = None
    correction_drop.value = "Low"

vcard_ver = CustomDropdown("Version 3", ["Version 2.1", "Version 3"], "VCard Version")
encrypt_drop = CustomDropdown("WPA/WPA2", ["None", "WEP", "WPA/WPA2"], "Network type", width=575)
crypto_drop = CustomDropdown("Bitcoin", ["Bitcoin", "Bitcoin Cash", "Ethereum", "Litecoin", "Dash"], "Select Cryptocurrency")
payment_drop = CustomDropdown(None, ["Buy now", "Add to cart", "Donation"], "Payment type", width=360)
correction_drop = CustomDropdown("Low", ["Low", "Medium", "High", "Very High"], "Correction Level")
gradiant_drop = CustomDropdown("Radial Gradient", ["Radial Gradient", "Square Gradient", "Horizontal Gradient", "Vertical Gradient"], "Gradient Styles")
#inner_eye_gradiant_drop = CustomDropdown("Solid Color", ["Solid Color", "Radial Gradient", "Square Gradient", "Horizontal Gradient", "Vertical Gradient"], "Color Styles")
#outer_eye_gradiant_drop = CustomDropdown("Solid Color", ["Solid Color", "Radial Gradient", "Square Gradient", "Horizontal Gradient", "Vertical Gradient"], "Color Styles")