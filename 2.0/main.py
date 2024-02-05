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
        if page.route == "home":
            home.main(page)
        elif page.route == "gui":
            gui()
            
    page.on_route_change = change_page
    page.go("home")
if __name__ == "__main__":
    flet.app(main)
