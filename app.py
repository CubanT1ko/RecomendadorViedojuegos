from flask import Flask, render_template, request
from scraper import search_rawg_games, get_rawg_game_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    platform = request.form['platform']
    genre = request.form['genre']
    favorite_games = request.form.getlist('favorite_games')

    api_key = "114a0f357a2e4de3a4f7bc9f2bdbad74"  # Reemplaza con tu clave API
    recommended_games = []

    for game in favorite_games:
        # Busca juegos en RAWG según el nombre del juego favorito
        search_results = search_rawg_games(game, api_key)

        if not search_results:
            print(f"No se encontraron resultados para: {game}")  # Mensaje si no hay resultados

        for result in search_results:
            app_id = result['app_id']
            game_details = get_rawg_game_details(app_id, api_key)
            if game_details:
                recommended_games.append(game_details)

    if not recommended_games:
        print("No se encontraron juegos recomendados.")  # Mensaje si no se encuentran recomendaciones

    return render_template('index.html', recommended=recommended_games)

if __name__ == '__main__':
    app.run(debug=True)
