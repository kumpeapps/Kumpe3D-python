"""Functions to Print Product Labels"""

import setup  # pylint: disable=unused-import, wrong-import-order
import os
import asyncio
import easygui
from beepy import beep
from pyhtml2pdf import converter
import params


def generate_pdf(url, pdf_path):
    """Generate PDF from URL"""
    converter.convert(
        url,
        pdf_path,
        print_options={
            "marginBotton": 0,
            "marginTop": 0,
            "marginLeft": 0,
            "marginRight": 0,
            "paperHeight": 1.97,
            "paperWidth": 3.15,
        },
    )


# Run the function
def generate_label(sku: str):
    """Generate PDF Product Label"""
    generate_pdf(
        "https://www.kumpe3d.com/product_labels.php?sku=" + sku,
        "label.pdf",
    )


def print_label():
    """Print Product Label PDF to Printer"""
    # Only print in production environment
    if params.app_env == "prod":
        os.system(
            "lp -d Product_Label_Printer -o media=50x80mm -o orientation-requested=4 label.pdf"
        )


def print_label_only():
    """Prints Product Label"""
    title = "Print Product label"
    msg = "Scan Product SKU to Print Product Label"

    while True:
        sku = easygui.enterbox(msg, title)
        if sku is None:
            break
        try:
            generate_label(sku)
            print_label()
            beep(1)
        except KeyError:
            beep(3)
            easygui.msgbox(f"Invalid SKU {sku}")


if __name__ == "__main__":
    generate_label("ALO-POO-LSN-L01")
