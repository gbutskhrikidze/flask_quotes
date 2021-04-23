from flask import Flask, render_template, request, redirect
import sqlite3
from flask.helpers import url_for
import folium
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)



@app.route('/')
def base():
    conn = sqlite3.connect('quotes.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from webdata")
    datas = cur.fetchall();
    conn.close()
    return render_template('index.html', datas = datas)

@app.route('/folium')
def maps():
    start_coords = (42, 43)
    folium_map = folium.Map(location=start_coords, zoom_start=8)
    folium_map.save('templates/folmap.html')
    return render_template('maps.html')

@app.route('/', methods=['GET', 'POST'])
def search():
    a = request.form['search-input']
    conn = sqlite3.connect('quotes.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from webdata where content=? or name=?", (a,a))
    datas = cur.fetchall();
    conn.close()
    return render_template("search.html", datas = datas)

"""@app.route('/', methods=['GET', 'POST'])
def query_search():
    a = request.form['search-input']
    return redirect(url_for("search"), a=a)"""


if __name__== '__main__':
    app.run(debug=True)