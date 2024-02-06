import psycopg2

conn = psycopg2.connect(database='netology_hw', user='postgres', password='4229887')
with conn.cursor() as cur:
    cur.execute('DROP TABLE test;')
    # cur.execute('CREATE TABLE test(id SERIAL PRIMARY KEY);')


    conn.commit()


conn.close()
