from widgets.main_page import *

def main(page: ft.Page):
    page.title = "Lemon-QRCodeMaker"
    #page.bgcolor = ft.colors.AMBER
    page.add(App())

if __name__ == "__main__":
    ft.app(target = main)