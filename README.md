Registro y visualización de notas
Proyecto sencillo para registrar notas de un estudiante desde una página web, guardar los datos en un archivo JSON y generar un reporte HTML con una gráfica de barras usando Python.

Características
Entrada de datos en HTML: Nombre y cinco asignaturas.

Guardado en JSON: Selección de ubicación del archivo en el navegador.

Procesamiento con Python: Lectura del JSON, cálculo de promedio y generación de gráfica.

Reporte HTML: Tabla de notas, promedio y una imagen de la gráfica.

Requisitos
Frontend: Navegador moderno con soporte para File System Access API (Chrome/Edge).

Backend (procesamiento):

Python 3.8+

pandas

matplotlib

Instalación de dependencias:

bash
pip install pandas matplotlib
Estructura del proyecto
Código
.
├── index.html
├── notas.json
├── procesar_notas.py
├── grafica.png
└── resultado.html
index.html: Formulario para capturar y guardar notas en notas.json.

procesar_notas.py: Script que genera grafica.png y resultado.html.

notas.json: Archivo generado con los datos del estudiante.

grafica.png: Imagen con la gráfica de barras.

resultado.html: Reporte final.

Uso
1. Capturar notas y guardar JSON
Abre index.html en el navegador.

Ingresa el nombre y las notas.

Haz clic en “Guardar en JSON”.

Elige la ubicación y guarda como notas.json.

2. Generar gráfica y reporte
Ejecuta el script de Python en la misma carpeta donde guardaste notas.json:

bash
python procesar_notas.py
Se crearán grafica.png y resultado.html.

Formato del JSON
Ejemplo de notas.json:

json
{
  "Nombre": "Ana Pérez",
  "Matemáticas": 8.5,
  "Lenguaje": 7.9,
  "Ciencias": 9.2,
  "Historia": 8.0,
  "Inglés": 8.7
}
Usa números entre 0 y 10 para las notas.

Respeta los nombres de las claves (incluyen acentos y mayúsculas).

Problemas comunes
El navegador no guarda el archivo: Usa Chrome o Edge; la File System Access API no funciona completo en todos los navegadores.

Promedio muestra NaN: Alguna nota no es numérica. Revisa que los campos tengan números.

No encuentra notas.json: Verifica que procesar_notas.py se ejecute en la misma carpeta donde guardaste el JSON.

Licencia
Este proyecto está disponible bajo la licencia MIT. Puedes usarlo y modificarlo libremente.
