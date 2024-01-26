import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

def launch():
    ft.app(target=main)

if __name__ == "__main__":
    launch()