import psycopg2 as psql


class Reports:
    """Movie class initializes with a title, image url, and trailer url"""

    def __init__(self):
        self.db = psql.connect("dbname=news")

    def generate_report(self):
        return ""

    def get_top_articles(self):
        cur = self.db.cursor()
        query = """select a.title, count(l.article_slug) as views
                    from articles a
                    left join article_log l on a.slug=l.article_slug
                    group by a.title
                    order by views DESC
                    LIMIT 3;
                """
        cur.execute(query)
        print(cur.fetchall())