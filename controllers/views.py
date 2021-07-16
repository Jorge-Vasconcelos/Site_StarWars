from flask import render_template, url_for, request, redirect
from app import app
import requests


@app.route('/')
def index():
    table = requests.get('http://127.0.0.1:5000/api/planets')
    planet_list = table.json()
    return render_template('lista.html', titulo='Jogos',
                           planets=planet_list)


@app.route('/new')
def site_new():
    return render_template('novo.html', titulo='New Game')


@app.route('/creat', methods=['POST', ])
def creat():
    name = request.form['name']
    climate = request.form['climate']
    terrain = request.form['terrain']
    payload = {'name': name,
               'climate': climate,
               'terrain': terrain}
    requests.post('http://127.0.0.1:5000/api/planet', json=payload)
    return redirect(url_for('index'))


@app.route('/delete/<string:id_planet>')
def site_delete(id_planet):
    requests.delete(f'http://127.0.0.1:5000/api/planet/{id_planet}')
    return redirect(url_for('index'))