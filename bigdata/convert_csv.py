import psycopg2
import os
from dotenv import load_dotenv

def convert(query):
    with open('sentences.csv','w') as f:
        f.write('id,sentence,word\n')
        for row in query:
            id, sentence, word = row
            f.write('{},{},{}\n'.format(id, sentence, word))
    return 'ok'


if __name__ == '__main__':
    try:
        load_dotenv(os.path.join(os.path.dirname(__file__),'.env'))
        dburl = os.environ.get('DATABASE_URL')
        conn = psycopg2.connect(dburl, sslmode='require')
    except:
        print('can not connect to db.')
        exit()
    sql = "select * from words"
    with conn.cursor() as cur:
        cur.execute(sql)
        query = cur.fetchall()
        print(convert(query=query))