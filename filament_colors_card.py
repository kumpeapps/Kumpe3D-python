import setup  # pylint: disable=unused-import, wrong-import-order
import os
import asyncio
import easygui
from beepy import beep
from pyppeteer import launch


async def generate_pdf(url, pdf_path):
    browser = await launch(options={"args": ["--no-sandbox"]})
    page = await browser.newPage()

    await page.goto(url)

    await page.pdf({"path": pdf_path, "width": "3.15in", "height": "1.97in"})

    await browser.close()


# Run the function
def generate_label(sku: str):
    asyncio.get_event_loop().run_until_complete(
        generate_pdf(
            "https://www.kumpe3d.com/filament_colors_card.php?sku=" + sku,
            "label.pdf",
        )
    )


def print_label():
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
