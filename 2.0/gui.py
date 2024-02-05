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
from params import Params


def gui():
    """Kumpe3D Admin GUI"""
    # beep(5)
    while True:
        cur_dir = os.getcwd()
        image = os.path.join(cur_dir, "logo.bmp")
        msg = "Select Program"
        choices = []
        if Params.Access.product_stock:
            choices.append("Add to Stock")
        if Params.Access.filament_stock:
            choices.append("Add Filament Roll")
            if not Params.Access.orders_desk:
                choices.append("Open Filament Roll")
                choices.append("Empty Filament Roll")
        if Params.Access.production:
            if Params.Access.print_room or Params.Access.admin:
                choices.append("Production Queue")
        if Params.Access.product_stock and Params.Access.print_labels:
            choices.append("Add to Stock & Print Label")
        if Params.Access.print_labels:
            choices.append("Print Product Label")
        if Params.Access.admin:
            if not Params.Access.orders_desk:
                choices.append("Print Filament Colors Card")

        program = easygui.buttonbox(msg, image=image, choices=choices)
        if program is None:
            # beep(7)
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
