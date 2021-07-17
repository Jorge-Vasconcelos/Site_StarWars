from flask import render_template, url_for, request, redirect
from app import app
import requests


@app.route('/')
def index():
    table = requests.get('http://127.0.0.1:5000/api/planets')
    planet_list = table.json()
    return render_template('index.html', titulo='Planets',
                           planets=planet_list)


@app.route('/new')
def new():
    return render_template('new.html', titulo='New Planet')


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


@app.route('/edit/<string:id_planet>')
def edit(id_planet):
    req = requests.get(f'http://127.0.0.1:5000/api/planet/{id_planet}')
    planet = req.json()
    print(planet)
    print(type(planet))
    planet = planet[0]  # list --> dictionary
    return render_template('edit.html', titulo='Planet Update',
                           planet=planet)


@app.route('/update', methods=['POST', ])
def update():
    id_planet = request.form['id_planet']
    name = request.form['name']
    climate = request.form['climate']
    terrain = request.form['terrain']
    payload = {'name': name,
               'climate': climate,
               'terrain': terrain}
    requests.put(f'http://127.0.0.1:5000/api/planet/{id_planet}', json=payload)
    return redirect(url_for('index'))


@app.route('/delete/<string:id_planet>')
def delete(id_planet):
    requests.delete(f'http://127.0.0.1:5000/api/planet/{id_planet}')
    return redirect(url_for('index'))
