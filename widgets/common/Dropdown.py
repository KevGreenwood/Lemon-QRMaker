import flet as ft

# Listas de opciones para Dropdowns
vcard_options = ["Version 2.1", "Version 3"]
encrypt_options = ["None", "WEP", "WPA/WPA2"]
crypto_options = ["Bitcoin", "Bitcoin Cash", "Ethereum", "Litecoin", "Dash"]
payment_options = ["Buy now", "Add to cart", "Donations"]
correction_options = ["Low", "Medium", "High", "Very High"]

# Función para crear Dropdown
def create_dropdown(value, options, label, width=None):
    return ft.Dropdown(
        value=value,
        options=[ft.dropdown.Option(option) for option in options],
        label=label,
        width=width
    )

# Creación de Dropdowns
vcard_ver = create_dropdown("Version 3", vcard_options, "VCard Version")
encrypt_drop = create_dropdown("WPA/WPA2", encrypt_options, "Network type", width=575)
cypto_drop = create_dropdown("Bitcoin", crypto_options, "Select Cryptocurrency")
payment_drop = create_dropdown(None, payment_options, "Payment type", width=360)
correction = create_dropdown("Low", correction_options, "Correction Level")