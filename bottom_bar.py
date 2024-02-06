"""Bottom Bar"""

import flet as ft
from libgravatar import Gravatar  # pylint: disable=import-error
from params import Params
from add_roll import add_roll
from open_roll import open_roll
from empty_roll import empty_roll
from gui import gui
from menu import load_menu


def bottom_bar(page: ft.Page):
    """Add Menu Bar"""

    def show_drawer(_):
        """Show Menu"""
        page.drawer.open = True
        page.drawer.update()

    load_menu(page)
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.GREEN,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU, icon_color=ft.colors.WHITE, on_click=show_drawer
                ),
                ft.Container(expand=True),
            ]
        ),
    )