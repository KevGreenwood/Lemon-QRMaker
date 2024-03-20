from flet import *
import flet as ft
from core import *
from main_designer import *

def main(page: Page):
    page.title = "Cassie-QRCodeMaker"
    page.horizontal_alignment = alignment.center
    page.add(QR_Tabs())


if __name__ == "__main__":
    app(target=main)