"""Bottom Bar"""

import flet as ft
from libgravatar import Gravatar  # pylint: disable=import-error
from params import Params
from add_roll import add_roll
from open_roll import open_roll
from empty_roll import empty_roll
from gui import gui


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

def load_menu(page: ft.Page):
    """Load Side Menu"""
    gravatar = Gravatar(Params.Access.email)
    avatar = ft.CircleAvatar(
        foreground_image_url=gravatar.get_image(default="mp"),
        content=ft.Text(Params.Access.username),
    )
    avatar_container = ft.Container(
        content=avatar,
        alignment=ft.alignment.top_center,
    )
    name_container = ft.Container(
        content=ft.Text(Params.Access.name), alignment=ft.alignment.top_center
    )

    def page_change(_):
        index = page.drawer.selected_index

        if index == 1:
            gui()
        bottom_bar(page)

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Row(
                controls=[avatar_container, name_container],
                alignment=ft.alignment.top_center,
            ),
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Logout",
                icon=ft.icons.LOGOUT,
                selected_icon_content=ft.Icon(ft.icons.LOGOUT_OUTLINED),
            ),
            ft.Divider(thickness=2),
        ],
        on_change=page_change,
    )
    if Params.Access.product_stock:
        page.drawer.controls.append(
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.LIBRARY_ADD),
                label="Add to Stock",
                selected_icon=ft.icons.LIBRARY_ADD_OUTLINED,
            )
        )
    if Params.Access.filament_stock:
        page.drawer.controls.append(
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ADD_BOX),
                label="Add Roll",
                selected_icon=ft.icons.ADD_BOX_OUTLINED,
            )
        )
        if not Params.Access.orders_desk:
            page.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.REMOVE_CIRCLE),
                    label="Open Roll",
                    selected_icon=ft.icons.REMOVE_CIRCLE_OUTLINE,
                )
            )
            page.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.DELETE_FOREVER),
                    label="Empty Roll",
                    selected_icon=ft.icons.DELETE_FOREVER_OUTLINED,
                )
            )
    if Params.Access.production:
        if Params.Access.print_room or Params.Access.admin:
            page.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.QUEUE),
                    label="Production Queue",
                    selected_icon=ft.icons.QUEUE_ROUNDED,
                )
            )
    if Params.Access.product_stock and Params.Access.print_labels:
        page.drawer.controls.append(
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.LIBRARY_ADD_CHECK),
                label="Add Stock & Print Label",
                selected_icon=ft.icons.LIBRARY_ADD_CHECK_OUTLINED,
            )
        )
    if Params.Access.print_labels:
        page.drawer.controls.append(
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PRINT),
                label="Print Lables",
                selected_icon=ft.icons.PRINT_OUTLINED,
            )
        )
    if Params.Access.admin:
        if not Params.Access.orders_desk:
            page.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PRINT),
                    label="Print Filament Card",
                    selected_icon=ft.icons.PRINT_OUTLINED,
                )
            )
