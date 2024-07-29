import flet as ft


class CustomDropdown(ft.Dropdown):
    def __init__(self, value, options, label, width=None):
        super().__init__()
        self.value=value
        self.options=[ft.dropdown.Option(option) for option in options]
        self.label=label
        self.width=width

vcard_ver = CustomDropdown("Version 3", ["Version 2.1", "Version 3"], "VCard Version")
encrypt_drop = CustomDropdown("WPA/WPA2", ["None", "WEP", "WPA/WPA2"], "Network type", width=575)
crypto_drop = CustomDropdown("Bitcoin", ["Bitcoin", "Bitcoin Cash", "Ethereum", "Litecoin", "Dash"], "Select Cryptocurrency")
payment_drop = CustomDropdown(None, ["Buy now", "Add to cart", "Donation"], "Payment type", width=360)
correction_drop = CustomDropdown("Low", ["Low", "Medium", "High", "Very High"], "Correction Level")

def reset_drop():
    vcard_ver.value = "Version 3"
    encrypt_drop.value = "WPA/WPA2"
    crypto_drop.value = "Bitcoin"
    payment_drop.value = None
    correction_drop.value = "Low"