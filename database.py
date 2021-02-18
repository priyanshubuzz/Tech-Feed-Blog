import psycopg2
import os

class Database():
    def __init__(self):
        self.conn = psycopg2.connect(
            database = "Tech Feed",
            user = "postgres",
            password = os.environ["postgre_pass"],
            host = "localhost"
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS article_data(id INT GENERATED ALWAYS AS IDENTITY ,article TEXT, image TEXT)")
    def add_content(self, article, img):
        self.cur.execute("INSERT INTO article_data(article, image) VALUES(%s, %s)", (article, img))
        self.conn.commit()
    def fetch_all(self):
        self.cur.execute("Select article FROM article_data")
        all_article = self.cur.fetchall()
        self.cur.execute("Select image FROM article_data")
        all_img = self.cur.fetchall() 
        all_data = all_article, all_img
        return all_data
    def fetch_PageData(self, page_id):
        self.cur.execute("SELECT * FROM article_data LIMIT 5 OFFSET %s", ((page_id-1) *5,))
        data = self.cur.fetchall()
        return data
    def __del__(self):
        self.conn.close()