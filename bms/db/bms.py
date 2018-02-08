import sqlite3

conn = sqlite3.connect(r'D:\workplace\bms\db\bms.db')

c = conn.cursor()

sql_01 = '''
	create table Genre
	(
		Name TEXT
	)
'''

sql_02 = '''
	create table Book
	(
		Title nvarchar(100),
		Author TEXT,
		GenreID INTGER,
		Cover TEXT,
		Price NUMERIC,
		Preface TEXT,
		IsValid BOOLEAN,
		PubDate DATETIME,
		FOREIGN KEY (GenreID) REFERENCES Genre(ROWID)
	)
'''

sql_03 = (
    "INSERT INTO Book VALUES ('Python 入门', 'Tom', 1, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('C# 入门', 'Bom', 2, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('ASP.net 入门', 'Com', 3, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('PHP 入门', 'Dom', 1, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('SQL Server 入门', 'Eom', 4, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('C++ 入门', 'Fom', 1, NULL, 39.00, '前言', 1, '2016-5-1')",
    "INSERT INTO Book VALUES ('Switch 入门', 'Gom', 2, NULL, 39.00, '前言', 1, '2016-5-1')"
)

sql_04 = (
    "INSERT INTO Genre VALUES ('计算机')",
    "INSERT INTO Genre VALUES ('文学艺术')",
    "INSERT INTO Genre VALUES ('外语学习')",
    "INSERT INTO Genre VALUES ('少儿读物')",
)

if __name__ == '__main__':
    c.execute(sql_01)
    c.execute(sql_02)
    for x in sql_04:
        c.execute(x)

    for m in sql_03:
        c.execute(m)