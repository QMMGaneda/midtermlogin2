from flask import Flask, jsonify, request
app = Flask(__name__)
movies = [
    {
        "name":"Iron Man",
        "casts":["Tony Stark", "Happy", "Jarvis", "Pepper Pots", "Iron Monger", "Rodey"],
        "genre":["Action", "Sci Fi", "Adventure", "Triller"]
    },
    {
        "name":"Iron Man 2",
        "casts":["Tony Stark", "Happy", "Jarvis", "Pepper Pots", "Rodey", "Whiplash", "Natasha Romanoff"],
        "genre":["Action", "Sci Fi", "Adventure", "Triller"]
    }
]
@app.route('/movies', methods=['Get'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return "The movie has been deleted", 200

if __name__ == '__main__':
    app.run()