from flet import *
import flet as ft
from core import *
from main_designer import *

def main(page: Page):
    page.title = "Cassie-QRCodeMaker"
    page.add(App())


if __name__ == "__main__":
    app(target=main)