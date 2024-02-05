"""Ship Order"""
import pymysql
import easygui
from beepy import beep
from helpers import get_sku_array
from params import Params


def ship_order():
    """Mark Order as Shipped"""
    title = "Mark Order as Shipped"
    msg = "Enter Order ID and Tracking Number"
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
            sku = get_sku_array(sku)
            sql = """INSERT INTO `Web_3dprints`.`stock`
                        (`sku`,
                        `swatch_id`,
                        `qty`)
                    VALUES
                        (%s, %s, 1)
                    ON DUPLICATE KEY UPDATE qty = qty + 1;"""
            cursor.execute(sql, (sku["base_sku"], sku["color"]))
            db.commit()
            beep(1)
        except KeyError:
            beep(3)


if __name__ == "__main__":
    ship_order()
