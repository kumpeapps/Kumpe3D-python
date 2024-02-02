"""Module for printing filament card labels"""
import setup  # pylint: disable=unused-import, wrong-import-order
import os
import asyncio
import easygui
from beepy import beep
import pdfkit


async def generate_pdf(url, pdf_path):
    """Generate PDF from URL"""
    options = {
        "page-width": "3.15in",
        "page-height": "1.97in",
        "margin-top": "0in",
        "margin-bottom": "0in",
        "margin-left": "0in",
        "margin-right": "0in",
        "print-media-type": "",
        "no-outline": "",
        "disable-smart-shrinking": "",
    }
    pdfkit.from_url(url, pdf_path, options=options)


# Run the function
def generate_label(sku: str):
    """Generate PDF Label"""
    asyncio.get_event_loop().run_until_complete(
        generate_pdf(
            "https://www.kumpe3d.com/filament_colors_card.php?color_id=" + sku,
            "label.pdf",
        )
    )


def print_label():
    """Print The Label"""
    os.system(
        "lp -d Product_Label_Printer -o media=50x80mm -o orientation-requested=4 label.pdf"
    )


def print_card():
    """Prints Filament Colors Card Label"""
    title = "Print Filament Colors Card label"
    msg = "Scan/Enter Color ID to Print Filament Colors Card Label"

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
            easygui.msgbox(f"Invalid Color ID {sku}")
