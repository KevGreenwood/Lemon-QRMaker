import flet as ft
import qrcode
import io
import base64

def main(page: ft.Page):
    page.title = "QR Code in Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data to QR encode')
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Convertir la imagen a una cadena de bytes
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')
    encoded_image = base64.b64encode(byte_arr.getvalue()).decode()

    # Mostrar la imagen en Flet
    page.add(ft.Image(encoded_image))

ft.app(main)
