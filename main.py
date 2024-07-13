from widgets.main_form import *

def main(page: ft.Page):
    page.title = "Lemon-QRCodeMaker"
    page.bgcolor = ft.colors.AMBER
    page.add(App())

if __name__ == "__main__":
    ft.app(target = main)