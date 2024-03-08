import flet as ft
import qrcode
import base64
from io import BytesIO
from PIL import Image


def main(page: ft.Page):
    page.title = "Cassie QRCode Generator"
    page.horizontal_alignment = "center"
    page.auto_scroll = True

    page.update()
    

    def generarQr(e):
        
        page.update()
        texto_error.value = ""
        texto_ok.value = ""
        contControles = len(page.controls)
        if txt.value == "":
            btn_guardar.disabled = True
            texto_error.value = "No hay texto para convertir a QR"
            texto_ok.value == ""
            # si hay 6 controles, es de una generacion previa, como no se 
            # escribio nada, elimina el ultimo control agregado que es la img del QR
            if contControles >= 6:
                page.controls.pop()
            page.update()
        else:
            texto_error.value = ""
            btn_guardar.disabled = False
            url = construyeQr(txt.value)
            img = ft.Image(src_base64=url)
            if contControles >= 6:
                page.controls.pop()
            texto_ok.value = "QR generado con exito"
            page.add(ft.Row([img]))
            page.update()
    
    def construyeQr(s):
        qr = qrcode.make(s)
        buffered = BytesIO()
        qr.save(buffered, format="JPEG")
        consBuff = base64.b64encode(buffered.getvalue())
        resultOfQrCode = consBuff.decode("utf-8")
        return resultOfQrCode
    
    def guardarImagen(e):
        url = construyeQr(txt.value)
        nombre_archivo = "qr_guardado.png"
        decodificarImg = base64.b64decode(url)
        img = Image.open(BytesIO(decodificarImg))
        img.save(nombre_archivo)
    

    def textbox_changed(e):
        if txt.value != "":
            btn.disabled = False
        else:
            btn.disabled = True
        page.update()

    txt = ft.TextField(label="Convertir a QR", multiline=True, on_change=textbox_changed)
    sizeField = ft.TextField(label="Ingrese un numero entero del 1 - 40")
    box_sizeField = ft.TextField(label="Ingrese un numero entero del 1 - 40")
    borderField = ft.TextField(label="Ingrese un numero entero del 1 - 40")
    errorDrop = ft.Dropdown(label="Selecciona el nivel de correcion de error", options=[ft.dropdown.Option("7%"), ft.dropdown.Option("15% (Default)"), ft.dropdown.Option("25%"), ft.dropdown.Option("30%")])
    qr_styleDrop = ft.Dropdown(label="Seleccione el estilo que desea aplicar", options=[ft.dropdown.Option("Normal"), ft.dropdown.Option("Gapped Square"), ft.dropdown.Option("Circle"), ft.dropdown.Option("Rounded"), ft.dropdown.Option("Vertical Bars"), ft.dropdown.Option("Horizontal Bars")])
    color_styleDrop = ft.Dropdown(label="Seleccione el estilo de color que desea aplicar", options=[ft.dropdown.Option("Normal"), ft.dropdown.Option("Radial Gradient"), ft.dropdown.Option("Square Gradient"), ft.dropdown.Option("Horizontal Gradient"), ft.dropdown.Option("Vertical Gradient"), ft.dropdown.Option("Image")])
    embed_imageBtn = ft.ElevatedButton("Seleccione su Imagen", icon=ft.icons.IMAGE_SEARCH)
    btn = ft.ElevatedButton("Generar QR",
                            on_click=generarQr, disabled=True, icon=ft.icons.QR_CODE)
    btn_guardar = ft.ElevatedButton("Guardar Imagen QR", on_click=guardarImagen, disabled=True, icon=ft.icons.SAVE_AS)
    logoBtn = ft.ElevatedButton("Seleccione su Logo", icon=ft.icons.IMAGE_SEARCH)
    
    
    texto_error = ft.Text(color="red")
    texto_ok = ft.Text(color="green")

    page.add(ft.Column([txt, ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls= [sizeField, box_sizeField, borderField]), ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls= [errorDrop, qr_styleDrop, color_styleDrop]), ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls= [logoBtn, embed_imageBtn]), btn, texto_error, texto_ok, btn_guardar]))

ft.app(target=main)