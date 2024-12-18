# Recomendador de Videojuegos

Este proyecto es un **Recomendador de Videojuegos** que permite a los usuarios encontrar juegos recomendados según sus preferencias de plataforma y género. La aplicación utiliza la API de RAWG para obtener información sobre los juegos, incluyendo detalles como el título, la calificación, la fecha de lanzamiento y las imágenes.

## Características

- Interfaz atractiva y amigable con estilo gamer.
- Búsqueda de juegos por plataforma y género.
- Recomendaciones visualizadas en un carrusel interactivo.
- Uso de la API de RAWG para obtener datos actualizados sobre videojuegos.

## Tecnologías Utilizadas

- HTML
- CSS (incluyendo Owl Carousel para el carrusel)
- JavaScript (jQuery)
- Python (Flask) para el backend

## Instalación

1. **Clona el repositorio:**


2. **Instala las dependencias necesarias:**

Asegúrate de tener Python y pip instalados. Luego, instala Flask y cualquier otra dependencia necesaria:


3. **Configura tu API Key:**

Para utilizar la API de RAWG, necesitas una clave de API. Puedes obtenerla registrándote en [RAWG](https://rawg.io/apidocs).

Una vez que tengas tu API key, debes añadirla a tu archivo `config.py` o directamente en el código donde se realiza la llamada a la API. Por ejemplo:


4. **Ejecuta la aplicación:**

Para iniciar el servidor, ejecuta:


La aplicación estará disponible en `http://127.0.0.1:5000`.

## Uso

1. Abre tu navegador y dirígete a `http://127.0.0.1:5000`.
2. Selecciona la plataforma y el género que prefieras.
3. Marca tus juegos favoritos.
4. Haz clic en "Recomendar Juegos" para ver las recomendaciones.

## Contribuciones

Este proyecto es de uso libre y puedes contribuir mejorando su funcionalidad o diseño. Si deseas contribuir, por favor crea un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en este repositorio o contactarme directamente.

---

¡Disfruta explorando videojuegos!
