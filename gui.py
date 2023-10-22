"""Kumpe3D Admin GUI"""
import setup  # pylint: disable=unused-import, wrong-import-order
import easygui
from beepy import beep
from increment_sku import increment_sku


def gui():
    """Kumpe3D Admin GUI"""
    while True:
        image = "logo.png"
        msg = "Select Program"
        choices = [
            "Increment SKU",
            "Inventory",
            "Get Order",
            "Ship Order",
            "Update Order Status",
        ]
        program = easygui.buttonbox(msg, image=image, choices=choices)
        if program is None:
            beep(7)
            break
        elif program == "Increment SKU":
            increment_sku()
        else:
            beep(3)
        print(program)


if __name__ == "__main__":
    gui()
