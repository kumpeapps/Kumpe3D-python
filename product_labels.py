import setup
import asyncio
from pyppeteer import launch


async def generate_pdf(url, pdf_path):
    browser=await launch(options={'args': ['--no-sandbox']})
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


if __name__ == "__main__":
    generate_label("ALO-POO-LSN-L01")
