"""Main Function for Kumpe3D Kiosk"""

import flet_easy as fs
import flet as ft
from views.addroll import addroll
from views.login import login
from views.addstock import addstock
from views.openroll import openroll
from views.emptyroll import emptyroll
from views.productionq import productionq
from views.productlabel import printproductlabel
from core.config import ConfigApp
from core.params import Params

app = fs.FletEasy(route_init="/login", route_login="/login")


@app.login
def login_x(page: ft.Page):
    """Require Login Function"""
    dlg = ft.AlertDialog(
        title=ft.Text(
            f"Access Denied!!!\nYou do not have access to {page.title}",
            text_align=ft.TextAlign.CENTER,
        ),
        on_dismiss=lambda e: print("Dialog dismissed!"),
        adaptive=False,
        bgcolor=ft.colors.RED_300,
    )

    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.update()

    if not Params.Access.basic:
        open_dlg()
        return False

    match page.title:
        case "Add Filament Roll":
            if Params.Access.basic:
                return True
            else:
                return False
        case "Empty Filament Roll" | "Open Filament Roll":
            if Params.Access.basic and Params.Access.filament_stock:
                return True
            elif Params.Access.admin:
                return True
            else:
                return False
        case "Add To Stock":
            if Params.Access.admin:
                return True
            elif Params.Access.basic and Params.Access.production:
                return True
            else:
                return False
        case "Production Queue":
            if Params.Access.admin:
                return True
            elif Params.Access.basic and Params.Access.production:
                return True
            elif Params.Access.basic and Params.Access.orders:
                return True
            else:
                return False
        case "Add to Stock & Print Label":
            if Params.Access.basic and Params.Access.print_labels:
                if Params.Access.admin:
                    return True
                elif Params.Access.production:
                    return True
            return False
        case "Print Product Label":
            if Params.Access.basic and Params.Access.print_labels:
                if Params.Access.admin:
                    return True
                elif Params.Access.production:
                    return True
            return False
        case "Print Filament Colors Card":
            if Params.Access.basic and Params.Access.print_labels:
                if Params.Access.admin:
                    return True
            return False
    return False


app.add_pages(
    [login, addstock, addroll, openroll, emptyroll, productionq, printproductlabel]
)
ConfigApp(app)

# We run the application
app.run()
