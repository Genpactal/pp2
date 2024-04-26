import psycopg2
conn = psycopg2.connect(
	database="snake",
	user='snake_user',
	password='Esko28:)',
	host='localhost',
	port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE Snakedata(
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
print("Database has been created successfully !!");
conn.close()