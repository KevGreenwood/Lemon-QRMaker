from main_form import *

def main(page: Page):
    page.title = "Cassie-QRCodeMaker"
    page.add(App())

if __name__ == "__main__":
    app(target = main)