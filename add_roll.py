"""Add Roll"""
import pymysql
import easygui
from beepy import beep
from params import Params


def add_roll():
    """Add's Roll to Stock"""
    title = "Add Filament Roll to Stock"
    msg = "Scan Filament SKU"
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
            sql = """
                UPDATE filament
                SET
                    instock = 1,
                    backorder = 0,
                    discontinued = 0,
                    full_rolls_instock = full_rolls_instock + 1,
                    coming_soon = 0
                WHERE manufacture_barcode = %s;
            """
            cursor.execute(sql, (sku))
            db.commit()
            verify_sql = """
                SELECT
                    idfilament,
                    swatch_id
                FROM filament
                WHERE 1=1
                    AND manufacture_barcode = %s
            """
            cursor.execute(verify_sql, sku)
            filament = cursor.fetchone()
            int(filament['idfilament'])
            beep(1)
        except (KeyError, TypeError):
            beep(3)
            easygui.msgbox(f"Invalid SKU {sku}")
