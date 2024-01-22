import setup
import asyncio
from pyppeteer import launch
import os


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
            "https://www.kumpe3d.com/product_labels.php?sku=" + sku,
            "label.pdf",
        )
    )


def print_label():
    os.system(
        "lp -d Product_Label_Printer -o media=50x80mm -o orientation-requested=4 label.pdf"
    )


if __name__ == "__main__":
    generate_label("ALO-POO-LSN-L01")
