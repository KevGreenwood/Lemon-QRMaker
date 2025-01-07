from main_page import App
from flet import (Page, app)

def main(page: Page):
    page.title = "Lemon-QRCodeMaker"
    #page.bgcolor = ft.Colors.AMBER
    page.scroll = "auto"
    page.add(App())

if __name__ == "__main__":
    app(main)