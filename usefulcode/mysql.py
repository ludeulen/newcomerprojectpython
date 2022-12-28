import MySQLdb

from sqlalchemy import create_engine


def update(name):
    db = MySQLdb.connect(host='localhost', port=3306, user='root', password='1234')

    cursor = db.cursor()

    sql = 'create database if not exists projectdb'

    cursor.execute(sql)

    db.commit()
    db.close()

    engine = create_engine("mysql+mysqldb://root:1234@localhost:3306/projectdb", encoding='utf-8')
    conn = engine.connect()

    df = name

    df.to_sql(name='', con=engine, if_exists='append', index=False)
    conn.close()

    return "전송 성공"
