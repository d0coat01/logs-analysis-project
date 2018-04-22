import psycopg2 as psql


class Reports:
    """Movie class initializes with a title, image url, and trailer url"""

    def __init__(self):
        self.db = psql.connect("dbname=news")

    def print_report(self):

        """Create a text-based report."""
        # Used (\n) for line separations instead of triple quotes for easy-to-read code.
        print(("\n"
               "**********************************\n"
               "* Analysis of Newspaper Articles *\n"
               "**********************************\n"))
        # Printed each function separately so you wouldn't have to wait for all queries to finish before seeing result.
        print(self.get_top_articles())
        print(self.get_top_authors())
        print(self.get_days_with_errors())
        print("**********************************\n"
              "*         End of Analysis        *\n"
              "**********************************\n")

    def get_top_articles(self):

        """Get the top 3 articles based on their occurrences in article_log"""
        # View alert: Used a view called article_log.
        # article_log is every log whose path contains "/articles/".
        # The path in article_log is changed to reflect an article slug when possible.
        # We can join on article_log and article now to get the top 3 articles.
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

        """Get the top authors based on their occurrences in article_log"""
        # This is similar to top articles except we use the authors table for grouping and selection.
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

        """Get all days that have more than 1% of their requests end in errors."""
        # Created two views here. One with the total # of requests for each day.
        # The other with the number of errors in each day.
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
reports.print_report()
reports.close()
