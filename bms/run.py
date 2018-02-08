import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

base_path = os.path.split(os.path.abspath(__name__))[0]
database = os.path.join(base_path, 'db/bms.db')


@app.route('/')
@app.route('/books/')
def book_list():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    books = c.execute(
        'SELECT Book.ROWID,Book.Title,Genre.name,Book.Author,Book.Price,Book.Isvalid,Book.PubDate FROM Book INNER JOIN Genre ON Book.GenreID = Genre.ROWID').fetchall()
    conn.close()
    return render_template('book-list.html', books=books)


@app.route('/book/edit/<int:id>/', methods=['GET', 'POST'])
def book_edit(id):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    if request.method == 'POST':
        data = (
            request.form.get('title', None),
            request.form.get('genreid', 1),
            request.form.get('author', None),
            request.form.get('cover', None),
            request.form.get('preface', None),
            request.form.get('price', None),
            request.form.get('isvalid', False),
            request.form.get('pubdate', None),
            id
        )
        c.execute(
            'UPDATE Book SET Title=?,GenreID=?,Author=?,Cover=?,Preface=?,Price=?,IsValid=?,PubDate=? WHERE ROWID=?', data)
        conn.commit()
        conn.close()
        return redirect(url_for('book_list'))
    else:

        book = c.execute(
            'SELECT Title,GenreID,Author,Cover,Preface,Price,IsValid,PubDate FROM Book WHERE ROWID= ?', [id]).fetchone()
        return render_template('book-edit.html', book=book)


@app.route('/book/del/<int:id>/')
def book_delete(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
