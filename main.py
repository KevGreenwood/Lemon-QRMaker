from flet import *
import flet as ft
from core import *
from main_designer import *

def main(page: Page):
    page.title = "Cassie-QRCodeMaker"
    left_side = Column([QR_Tabs(), LeftLayout()])
    page.add(Row([left_side, RightLayout()], alignment=MainAxisAlignment.CENTER, vertical_alignment=CrossAxisAlignment.START))


if __name__ == "__main__":
    app(target=main)