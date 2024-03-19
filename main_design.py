from flet import *
import flet as ft
from core import *

class Input(UserControl):
    def __init__(data: str, ):
        super().__init__()
        self.data = data
