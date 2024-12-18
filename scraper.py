import requests

def get_rawg_game_details(game_id, api_key):
    url = f"https://api.rawg.io/api/games/{game_id}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return {
                'title': data['name'],
                'price': "N/A",  # RAWG no proporciona precios directamente
                'link': data['website'] if 'website' in data else f"https://rawg.io/games/{game_id}",
                'released': data.get('released', 'N/A'),
                'rating': data.get('rating', 'N/A'),
                'image': data.get('background_image', 'N/A')  # Añadir la URL de la imagen
            }
        except ValueError as e:
            print(f"Error al decodificar JSON: {e}")
            print("Respuesta:", response.text)
    else:
        print(f"Error al obtener detalles del juego: {response.status_code} - {response.text}")
    return None

def search_rawg_games(query, api_key):
    url = "https://api.rawg.io/api/games"
    params = {
        'key': api_key,
        'page_size': 10,
        'search': query
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            games = []
            
            for game in data['results']:
                app_id = game['id']
                title = game['name']
                games.append({'app_id': app_id, 'title': title})

            return games
        except ValueError as e:
            print(f"Error al decodificar JSON: {e}")
            print("Respuesta:", response.text)
    else:
        print(f"Error en la solicitud: {response.status_code} - {response.text}")
    
    return []
