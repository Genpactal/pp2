import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='6618',
	host='localhost',
)

''' create or replace function getAllPhone(lim integer, ofs integer )
       returns setof Phonebook
        as
        $$
        begin
           return query
           select * from Phonebook limit $1 offset $2;
        end;  
        $$ language plpgsql;
        select *
        from getAllPhone(1,2);'''

cursor = conn.cursor()
conn.autocommit = True
limit = int(input("Limit: "))
offset = int(input("Offset: "))

cursor.callproc('getAllPhone', (limit, offset))
result = cursor.fetchall()
print(result)