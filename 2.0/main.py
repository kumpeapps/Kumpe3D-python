"""Kumpe3D Kiosk"""

import flet as ft
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import home
from gui import gui
from params import Params
from bottom_bar import bottom_bar


def main(page: Page):
    page.title = "Kumpe3D Kiosk"
    bottom_bar(page)

    def change_page(_):
        page.drawer.open = False
        if page.route == "home":
            home.main(page, True)
            page.update()
        elif page.route == "gui":
            home.main(page, False)
            page.update()
        elif page.route == "logout":
            page.bottom_appbar.visible = False
            Params.Access.set_access_level("unauthenticated")
            home.main(page, True, True)
            page.update()

    page.on_route_change = change_page
    page.go("logout")


if __name__ == "__main__":
    flet.app(main)
