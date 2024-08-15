from widgets.main_page import (ft, App)

def main(page: ft.Page):
    page.title = "Lemon-QRCodeMaker"
    #page.bgcolor = ft.colors.AMBER
    page.add(App())

if __name__ == "__main__":
    ft.app(main)