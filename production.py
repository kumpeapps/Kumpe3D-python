"""Production"""
import pymysql
import easygui
from beepy import beep
from params import Params


def production_queue():
    """Get Production Queue"""
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """
        SELECT 
            CONCAT(sku, '-', swatch_id) AS sku,
            `name`,
            0 - qty AS qty
        FROM
            Web_3dprints.vw_stock__production_queue;
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    text = ""
    for result in results:
        row = f"\u2022x{int(result['qty'])} {result['sku']} ({result['name']})\n"
        text = text + row

    easygui.msgbox(text, "Production Queue")

if __name__ == "__main__":
    production_queue()
