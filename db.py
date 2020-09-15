import sqlite3
import re
import os

dbname = os.environ.get('LINK_SHORTENER_DBNAME')

with sqlite3.connect(dbname) as conn:
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS links(
            id integer primary key autoincrement unique,
            link text not null,
            postfix varchar(10) not null unique
        )
        """)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def addLink(linkToRedirect, generatedLink):
    with sqlite3.connect(dbname) as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()
        if not re.match('(?:http|ftp|https)://', linkToRedirect):
            linkToRedirect = f'http://{linkToRedirect}'
        c.execute(
            f"INSERT INTO links(link,postfix) values('{linkToRedirect}','{generatedLink}')")
        conn.commit()


def getLink(postfix):
    with sqlite3.connect(dbname) as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(f"SELECT * FROM links WHERE postfix='{postfix}'")
        data = c.fetchone()
        if data:
            fetchedLink = data.get('link')
        else:
            fetchedLink = None
        return fetchedLink
