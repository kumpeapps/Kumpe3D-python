import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()
    btn = ft.ElevatedButton("Click me!")
    page.add(btn)


# "Add to Stock",
#             "Add Filament Roll",
#             "Open Filament Roll",
#             "Empty Filament Roll",
#             "Production Queue",
#             "Add to Stock & Print Label",
#             "Print Product Label",
#             "Print Filament Colors Card",
def launch():
    ft.app(target=main)

if __name__ == "__main__":
    launch()