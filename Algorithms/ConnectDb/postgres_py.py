import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = '123456'
port_id = 5433
conn = None
cur = None
try:
    with psycopg2.connect(
        host = hostname, 
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            script = '''
            SELECT * FROM film
            '''
            cur.execute(script)
            for record in cur.fetchall():
                print(record['title'],record['length'])
except Exception as e:
    print(e)
finally:

    if  conn:
        conn.close()




