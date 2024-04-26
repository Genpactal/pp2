import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='user',
        password='12345',
        port='54321'
    )

    conn.autocommit = True

    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS PhoneBook(
       first_name VARCHAR(255) NOT NULL,
       last_name VARCHAR(255),
       phone_num VARCHAR(20)
    )'''

    cursor.execute(sql)

    print("Database has been created")

except psycopg2.Error as e:
    print("Error:", e)

finally:
    if 'conn' in locals():
        conn.close()