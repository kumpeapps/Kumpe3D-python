"""Increment SKU"""
import pymysql
import easygui
from beepy import beep
from helpers import get_sku_array
from params import Params


def increment_sku():
    """Increments SKU Stock Qty"""
    title = "Increment SKU Stock Qty"
    msg = "Scan Product SKU"
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)

    while True:
        sku = easygui.enterbox(msg, title)
        if sku is None:
            cursor.close()
            db.close()
            break
        try:
            sku_array = get_sku_array(sku)
            sql = """INSERT INTO `Web_3dprints`.`stock`
                        (`sku`,
                        `swatch_id`,
                        `qty`)
                    VALUES
                        (%s, %s, 1)
                    ON DUPLICATE KEY UPDATE qty = qty + 1;"""
            cursor.execute(sql, (sku_array["base_sku"], sku_array["color"]))
            db.commit()
            beep(1)
        except KeyError:
            beep(3)
            easygui.msgbox(f"Invalid SKU {sku}")


if __name__ == "__main__":
    increment_sku()
