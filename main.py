"""Login Page V2"""
import setup  # pylint: disable=unused-import, wrong-import-order
import os
import socket
import requests
import flet as ft
from dotenv import load_dotenv
from gui import gui
import logo  # pylint: disable=import-error
from params import Params
from ip_host import get_ip

load_dotenv()
userid = os.getenv(key="USERID", default="")


def main(page: ft.Page):
    """Main Function"""
    img_container = ft.Container(
        content=ft.Image(src_base64=logo.logo_base64), alignment=ft.alignment.top_center
    )
    page.add(img_container)

    def did_login(_):
        send_request(username_field.value, password_field.value)
        page.update()

    password_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        autocorrect=False,
        enable_suggestions=False,
        prefix_icon=ft.icons.PASSWORD,
        on_submit=did_login,
    )

    def username_submit(_):
        """Activate Password Field on Submit"""
        password_field.focus()

    username_field = ft.TextField(
        label="Username",
        autofocus=True,
        autocorrect=False,
        enable_suggestions=False,
        prefix_icon=ft.icons.PERSON,
        on_submit=username_submit,
    )

    submit_container = ft.Container(
        content=ft.ElevatedButton(text="Login", on_click=did_login),
        alignment=ft.alignment.center,
    )
    page.update()
    page.add(username_field, password_field, submit_container)

    def show_banner_click(
        message: str,
        color: ft.colors = ft.colors.RED_400,
        icon: ft.icons = ft.icons.ERROR_ROUNDED,
    ):
        page.banner = ft.Banner(
            bgcolor=color,
            leading=ft.Icon(icon, color=ft.colors.RED_900, size=40),
            content=ft.Text(message),
            actions=[
                ft.TextButton("Dismiss", on_click=close_banner),
            ],
        )
        page.banner.open = True
        page.update()

    def close_banner(_):
        page.banner.open = False
        page.update()

    def send_request(username: str, password: str):
        """KumpeApps SSO Login"""
        # Login
        # GET https://www.kumpeapps.com/api/check-access/by-login-pass

        try:
            response = requests.get(
                url=f"{Params.KumpeApps.api_url}/check-access/by-login-pass",
                params={
                    "_key": Params.KumpeApps.api_key,
                    "login": username,
                    "pass": password,
                },
                timeout=10,
            )

            data = response.json()
            success = data["ok"]
            if not success:
                show_banner_click(data["msg"])
            else:
                subscriptions = data["subscriptions"]
                user_id = data["user_id"]
                is_admin = "213" in subscriptions
                is_basic = "214" in subscriptions
                is_orderfiller = "215" in subscriptions
                computername=socket.gethostname()
                if is_admin:
                    Params.Access.set_access_level("admin")
                    log_access(user_id, f"/{computername}/granted/admin")
                    gui()
                elif is_orderfiller:
                    Params.Access.set_access_level("order_filler")
                    log_access(user_id, f"/{computername}/granted/order_filler")
                    gui()
                elif is_basic:
                    Params.Access.set_access_level("basic")
                    log_access(user_id, f"/{computername}/granted/basic")
                    gui()
                else:
                    Params.Access.set_access_level("unauthenticated")
                    show_banner_click("Access Denied")
                    log_access(user_id, f"/{computername}/denied")
            password_field.value = ""

        except requests.exceptions.RequestException:
            show_banner_click(
                message="Unknown Error. This COULD mean you do not have an internet connection."
            )

    def log_access(user_id: str, note: str):
        # POST Access Log
        # POST https://www.kumpeapps.com/api/access-log

        try:
            _ = requests.post(
                url=f"{Params.KumpeApps.api_url}/access-log",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                },
                data={
                    "_key": Params.KumpeApps.api_key,
                    "user_id": user_id,
                    "referrer": "Kumpe3D Kiosk",
                    "url": note,
                    "remote_addr": format(
                        requests.get(
                            "https://api.ipify.org", timeout=10
                        ).content.decode("utf8")
                    ),
                },
                timeout=10,
            )
        except requests.exceptions.RequestException:
            print("HTTP Request failed")


# "Add to Stock",
#             "Add Filament Roll",
#             "Open Filament Roll",
#             "Empty Filament Roll",
#             "Production Queue",
#             "Add to Stock & Print Label",
#             "Print Product Label",
#             "Print Filament Colors Card",
def launch():
    """Initial Launch"""
    if userid == "0":
        Params.Access.set_access_level("basic")
        gui()
    else:
        ft.app(target=main)


if __name__ == "__main__":
    launch()
