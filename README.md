# Scrappeando ![image](https://github.com/user-attachments/assets/49106eed-9358-4b55-bd46-146989f06058)

## Descripción
Este proyecto recopila información y precios de Wallapop. Está optimizado para iphones. Las pruebas han sido hechas con los modelos de iPhone 14, 15 y 16.


## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto-ejemplo.git
2. Instala las librerias:
   ```bash
   pip install -r requirements.txt
3. Ejecuta el jupiter notebook wallascrap.ipynb. En la segunda celda puedes modificar los parametros para scrapear: selecciona ```Elemento a buscar``` ```Estado``` ```distancia``` ```n_scrolls_cada_vez```
 ```Lista a incluir```  ```Lista a excluir```
  Recomiendo modificar solamente ```Elemento a buscar``` ```Estado``` y ```distancia```. Ten en cuenta que el código está pensando para scrappear los elementos de Madrid
4. Ejecuta los jupiter 02_... y 03_...
5. El archivo 04_download_description.ipynb descarga los comentarios del elementos seleccionado. Se pueden seleccionar por número del iphone y por estado.
6. El archivo 05_get_batt_from_comments.ipynb selecciona número del iphone y estado y busca el estado de la bateria en el comentario del anuncio para complementar la tabla de estado de la batería
7. El archivo iphones tableau/wallapop.twb tiene algunas estadisticas interesantes. El Dashboard mostrado a continuación funciona de la siguiente manera:
- El color y el tamaño indica el estado de la batería, siendo 0 si no tiene estado.
- Se muestran box-plot con los rangos intercuartilicos para detectar outlayers
- Al posicionar el puntero sobre un punto se muestran las caracteristicas. Al hacer click, se abre el enlace web del anuncio
![image](https://github.com/user-attachments/assets/58e7e3ff-3a32-452c-bcbd-1526baf277f5)

## Puntos pendientes

1. Hacer un programa llame automaticamente los elementos que queremos scrappear para no tener que ejecutar los notebooks manualmente modificando variables.
2. Colocar lineas horizontales en los precios de los productos nuevos scrappeandolos de apple.com para mejorar la visualización.
3. Añadir caracteristicas:
   - Si está reservado
   - Si es de tienda o de particular
   - Si ya no existe
4. Analizar cuanto tiempo están en el mercado re-scrappeando cada x dias.
5. Hacer un modelo de ML para estimar el precio de un producto y analizar qué factores afectan más a su valor
6. Igual pero para predecir cuanto tiempo estará el producto en el mercado
