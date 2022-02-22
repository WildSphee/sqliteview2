import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("land.db")
    except Error:
        print(Error)

    return conn

def create_table(conn, table=None):
    try:
        sql = """
        CREATE TABLE Countries (
        country_id INTEGER NOT NULL PRIMARY KEY,
        country_name TEXT,
        land INTEGER
        );
        """
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        print("table created")
    except Exception:
        print("table already exist")

def new_country(conn, entry):
    sql = """
    INSERT INTO Countries (country_name, land) VALUES (?,?);
    """
    c = conn.cursor()
    c.execute(sql, entry)
    conn.commit()

def fetchadd(conn):
    c = conn.cursor()
    c.execute("""
       SELECT * FROM Countries ORDER BY country_id ASC
       """)
    fetch = c.fetchall()
    return fetch

def deleteCountry(conn, name=None, id=None):
    sql = ""
    if name is id is None:
        "please input either name or id"
        return
    elif name is not None:
        sql = f"""
        DELETE FROM Countries WHERE country_name="{name}";
        """
    elif id is not None:
        sql = f"""
        DELETE FROM Countries WHERE country_id={id};
        """
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

def deleteAllCountry(conn):
    sql = """
    DELETE FROM Countries
    """
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


#conn = create_connection()
#create_table(conn, table="randomtable")
#entry = ("USA", 186)
#new_country(conn, entry)
