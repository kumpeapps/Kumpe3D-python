"""Kumpe3D Admin GUI"""
import setup  # pylint: disable=unused-import, wrong-import-order
import os
import easygui
from beepy import beep
from increment_sku import increment_sku
from add_roll import add_roll
from open_roll import open_roll
from empty_roll import empty_roll
from production import production_queue
import product_labels
import filament_colors_card as fc_card
import beta.gui as beta


def gui():
    """Kumpe3D Admin GUI"""
    while True:
        cur_dir = os.getcwd()
        image = os.path.join(cur_dir, "logo.bmp")
        msg = "Select Program"
        choices = [
            "Add to Stock",
            "Add Filament Roll",
            "Open Filament Roll",
            "Empty Filament Roll",
            "Production Queue",
            "Add to Stock & Print Label",
            "Print Product Label",
            "Print Filament Colors Card",
        ]
        program = easygui.buttonbox(msg, image=image, choices=choices)
        if program is None:
            beep(7)
            break
        elif program == "Add to Stock":
            increment_sku()
        elif program == "Add Filament Roll":
            add_roll()
        elif program == "Open Filament Roll":
            open_roll()
        elif program == "Empty Filament Roll":
            empty_roll()
        elif program == "Production Queue":
            production_queue()
        elif program == "Add to Stock & Print Label":
            increment_sku(True)
        elif program == "Print Product Label":
            product_labels.print_label_only()
        elif program == "Print Filament Colors Card":
            fc_card.print_card()
        else:
            beep(3)
        print(program)


if __name__ == "__main__":
    gui()
