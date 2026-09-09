import pyodbc

# 连接字符串
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=shop;'
    'UID=sa;'
    'PWD=Lgj1110@'
)

# 连接
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# 增删改查示例
cursor.execute("SELECT * FROM Store")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


def get_db_connection():
    """获取数据库连接"""
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=shop;'
        'UID=sa;'
        'PWD=Lgj1110@'
    )
    return pyodbc.connect(conn_str)

# 查询数据
def query_data():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Store")
        return cursor.fetchall()

# 插入数据
def insert_data(name, address):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Store (Name, Address) VALUES (?, ?)",
            (name, address)
        )
        conn.commit()  # 记得提交事务

# 更新数据
def update_data(store_id, new_name):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Store SET Name = ? WHERE StoreID = ?",
            (new_name, store_id)
        )
        conn.commit()

# 删除数据
def delete_data(store_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Store WHERE StoreID = ?",
            (store_id,)
        )
        conn.commit()

# 使用示例
""" if __name__ == "__main__":
    # 查询
    rows = query_data()
    for row in rows:
        print(row) """