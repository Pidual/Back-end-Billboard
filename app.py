from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from music import Music
from bson.json_util import dumps

db = dbase.dbConnection()
#db.db()
app = Flask(__name__)

# Rutas de la aplicacion
@app.route('/')  # Primera ruta
def home():
    return "Welcome to the Billboard API!"

@app.route('/songs', methods=['GET'])
def get_songs():
    billboard_collection = db['billboard']
    data = list(billboard_collection.find())
    return Response(dumps(data), mimetype='application/json')

# CREATE
@app.route('/music', methods=['POST'])
def addSong():
    billboard_collection = db['billboard']
    rank = request.form['rank']
    song_name = request.form['song_name']
    singer = request.form['singer']
    last_week = request.form['last_week']
    peak_position = request.form['peak_position']
    weeks_on_chart = request.form['weeks_on_chart']

    if rank and song_name and last_week and singer and peak_position and weeks_on_chart:
        music = Music(rank, song_name, last_week, singer, peak_position, weeks_on_chart)
        billboard_collection.insert_one(music.toDBCollection())
        return redirect(url_for('home'))
    else:
        return notFound()

# Method DELETE
@app.route('/delete/<string:song_name>')
def delete(song_name):
    billboard_collection = db['billboard']
    billboard_collection.delete_one({'song_name': song_name})
    return redirect(url_for('home'))

# Method UPDATE
@app.route('/edit/<string:song_name>', methods=['POST'])
def edit(song_name):
    billboard_collection = db['billboard']
    rank = request.form['rank']
    new_song_name = request.form['song_name']
    singer = request.form['singer']
    last_week = request.form['last_week']
    peak_position = request.form['peak_position']
    weeks_on_chart = request.form['weeks_on_chart']

    if rank and new_song_name and last_week and singer and peak_position and weeks_on_chart:
        music = Music(rank, new_song_name, last_week, singer, peak_position, weeks_on_chart)
        billboard_collection.update_one(
            {'song_name': song_name},
            {'$set': {
                'Rank': rank,
                'Song Name': new_song_name,
                'Singer': singer,
                'Last Week': last_week,
                'Peak Position': peak_position,
                'Weeks on Chart': weeks_on_chart
            }}
        )
        return redirect(url_for('home'))
    else:
        return notFound()

# READ
@app.route('/song/year/<int:year>', methods=['GET'])
def get_events_by_year(year):
    filtered_data = [event for event in data_dict if event['Año'] == year]
    return jsonify(filtered_data)

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
