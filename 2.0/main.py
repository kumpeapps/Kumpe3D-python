"""Kumpe3D Kiosk"""

import flet as ft
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import home
from gui import gui


def main(page: Page):
    page.title = "Kumpe3D Kiosk"

    def change_page(_):
        page.clean()
        page.update()
        if page.route == "home":
            home.main(page)
            page.update()
        elif page.route == "gui":
            gui()
        elif page.route == "logout":
            page.clean()
            home.main(page)
            page.update()

    page.on_route_change = change_page
    page.go("home")


if __name__ == "__main__":
    flet.app(main)
