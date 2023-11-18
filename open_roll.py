"""Open Roll"""
import pymysql
import easygui
from beepy import beep
from params import Params


def open_roll():
    """Move Filament Roll from Full to Partial"""
    title = "Open Filament Roll"
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
                    full_rolls_instock = full_rolls_instock - 1,
                    partial_rolls_instock = partial_rolls_instock + 1
                WHERE manufacture_barcode = %s OR swatch_id = %s;
            """
            cursor.execute(sql, (sku, sku))
            db.commit()
            verify_sql = """
                SELECT
                    idfilament,
                    swatch_id
                FROM filament
                WHERE 1=1
                    AND (manufacture_barcode = %s OR swatch_id = %s)
            """
            cursor.execute(verify_sql, (sku, sku))
            filament = cursor.fetchone()
            int(filament['idfilament'])
            beep(1)
        except (KeyError, TypeError):
            beep(3)
            easygui.msgbox(f"Invalid SKU {sku}")
