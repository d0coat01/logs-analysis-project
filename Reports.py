import psycopg2 as psql


class Reports:
    """Movie class initializes with a title, image url, and trailer url"""

    def __init__(self):
        self.db = psql.connect("dbname=news")

    def generate_report(self):
        """Create a text-based report."""
        report = ("\n"
                  "**********************************\n"
                  "* Analysis of Newspaper Articles *\n"
                  "**********************************\n")
        report += self.get_top_articles()
        report += self.get_top_authors()
        report += self.get_days_with_errors()
        report += ("**********************************\n"
                   "*         End of Analysis        *\n"
                   "**********************************\n")
        return report

    def get_top_articles(self):
        cur = self.db.cursor()
        query = ("select a.title, count(l.article_slug) as views\n"
                 "from articles a\n"
                 "left join article_log l on a.slug=l.article_slug\n"
                 "group by a.title\n"
                 "order by views DESC\n"
                 "LIMIT 3;\n")
        cur.execute(query)
        results = cur.fetchall()
        report = ("\n"
                  "Top 3 Articles of All Time\n"
                  "\n")
        for result in results:
            report += '"' + result[0] + '" - ' + str(result[1]) + " views \n"
        cur.close()
        return report

    def get_top_authors(self):
        cur = self.db.cursor()
        query = ("select authors.name, count(article_log.article_slug) as views from authors\n"
                 "left join articles on authors.id = articles.author\n"
                 "left join article_log on articles.slug = article_log.article_slug\n"
                 "group by authors.name\n"
                 "order by views DESC;\n")
        cur.execute(query)
        results = cur.fetchall()
        report = ("\n"
                  "Top Authors of All Time\n"
                  "\n")
        for result in results:
            report += result[0] + ' - ' + str(result[1]) + " views \n"
        cur.close()
        return report

    def get_days_with_errors(self):
        cur = self.db.cursor()
        query = ("select to_char( e.date, 'Mon DD, YYYY') as date\n"
                 ",round((e.error_count::decimal/r.request_count::decimal) * 100, 1) as percent_errors\n"
                 "from daily_errors e, daily_requests r\n"
                 "where e.date = r.date\n"
                 "and (e.error_count::decimal/r.request_count::decimal) > 0.01\n"
                 "order by date DESC;\n")
        cur.execute(query)
        results = cur.fetchall()
        report = ("\n"
                  "Days Where 1% of Requests Lead to Errors\n"
                  "\n")
        for result in results:
            report += result[0] + ' - ' + str(result[1]) + "% errors\n"
        cur.close()
        return report

    def close(self):
        self.db.close()


reports = Reports()
print(reports.generate_report())
reports.close()
