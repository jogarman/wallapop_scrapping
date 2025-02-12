# Scrappeando ![image](https://github.com/user-attachments/assets/49106eed-9358-4b55-bd46-146989f06058)

## Descripción
Este proyecto recopila información y precios de Wallapop. Está optimizado para iphones y en menor medida gopros. Las pruebas han sido hechas con los modelos de iPhone 14, 15 y 16.


El archivo iphones tableau/wallapop.twb tiene algunas estadisticas interesantes. No se mejora por que carezco de lincencia de Tableu. El Dashboard mostrado a continuación funciona de la siguiente manera:
- El color y el tamaño indica el estado de la batería, siendo 0 si no tiene estado.
- Se muestran box-plot con los rangos intercuartilicos para detectar outlayers
- Al posicionar el puntero sobre un punto se muestran las caracteristicas. Al hacer click, se abre el enlace web del anuncio
![image](https://github.com/user-attachments/assets/58e7e3ff-3a32-452c-bcbd-1526baf277f5)

![image](https://github.com/user-attachments/assets/164ccd0f-47cc-45d4-9220-2066ed423a38)

## Makefile
convert- prepara la carpeta build desde src
docker_build -por probar
docker_run -por configurar
clean - elimina /build
git -sube todos los cambios a git

## Problemas
Los archivos principales gopro_scrapper.py y iphone_scrapper.py deben ejecutarse **SIEMPRE** moviendo el pwd a la carpeta build y haciendo "python gopro_scrapper.py"
No se puede automatizar con un script o con makefile porque estos ejecutan hijos en subprocesos y no pueden modificar el cwd de los futuros subprocesos que se crean al llamar. Llevo 3 horas intentandolo y es mejor hacer primero "cd build" y luego "python gopro_scrapper.py"

<