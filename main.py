"""
TODO API:
1. load_FIO
2. load_TG/num
3. city
4. impuls
5. alldone
TODO DB:
1. names
2. contacts
3. cities
4. impulses
TODO YARIK:(извини)
root get запрос
переадресация после post запроса
Смотри, как пример:
    def note_repr(key):
        return {
            'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
            'text': notes[key]
        }
А затем:
    return note_repr(idx), status.HTTP_201_CREATED
Взял отсюда https://github.com/flask-api/flask-api
+ надо проверить обработку пост запросов
"""
import sqlite3 as sql
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions


app = FlaskAPI(__name__)
conn = sql.connect(r'Database/answers.db')
cur = conn.cursor()
impulses = ['ЧТО', 'ТАКОЕ', 'ИМПУЛЬС'] #Вставить направления

@app.route("/", methods=['GET'])
def root():
    # сумерки сгущались и в какой-то миг похолодела кровь моя...
    return "index" #index.html
@app.route("/api/load-fio", methods=['POST'])
def fio():
    # фосфорные краски - я спектакль вам устрою...
    if request.method == 'POST':
        fio = str(request.data.get('text', ''))
        return status.HTTP_201_CREATED
@app.route("/api/load-cont", methods=['POST'])
def load_cont():
    # память о тебе как жвачка в волосах...
    if request.method == 'POST':
        cont = str(request.data.get('text', ''))
        if len(cont) == 12 and cont[0] == '+':
            return status.HTTP_202_ACCEPTED
        elif cont[0] == '@':
            return status.HTTP_202_ACCEPTED
        else:
            return status.HTTP_400_BAD_REQUEST
@app.route("/api/load-city", methods=['POST'])
def load_city():
    # битва - не война, стометровка - не марафон...
    if request.method == 'POST':
        city = str(request.data.get('text', ''))
        return status.HTTP_201_CREATED
@app.route("/api/load-impulse", methods=['POST'])
def load_impulse():
    # все они за одно, это западня....
    if request.method == 'POST':
        impulse = str(request.data.get('text', ''))
        for im in impulses
            if impulse == impulses[im]:
                return status.HTTP_202_ACCEPTED
        return status.HTTP_400_BAD_REQUEST



if __name__ == "__main__":
    app.run(debug=True)