import psycopg2
conn = psycopg2.connect(
	database="snake",
	user='postgres',
	password='6618',
	host='localhost',
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE snakedata(
   user_login VARCHAR(255) NOT NULL,
   last_score INT,
   last_level INT,
   last_FPS INT,
   snake_len INT,
   wall_len INT,
   snake_x INT,
   snake_y INT,
   record INT
);'''


cursor.execute(sql)
print("Database has been created successfully !!")
conn.close()