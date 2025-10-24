import pandas as pd
import matplotlib.pyplot as plt
import os

ruta_json = "notas.json"
ruta_html = "resultado.html"
ruta_img = "grafica.png"

if not os.path.exists(ruta_json):
    print("No se encontró el archivo notas.json")
else:
    notas = pd.read_json(ruta_json, typ="series")
    asignaturas = ["Matemáticas", "Lenguaje", "Ciencias", "Historia", "Inglés"]
    valores = [pd.to_numeric(notas[a], errors="coerce") for a in asignaturas]
    promedio = pd.Series(valores).mean()

    plt.bar(asignaturas, valores, color="#6C63FF")
    plt.title(f"Notas de {notas['Nombre']}")
    plt.ylabel("Nota")
    plt.ylim(0, 10)
    plt.savefig(ruta_img, bbox_inches="tight")
    plt.close()

    html = f"""
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Resultado de Notas</title>
    </head>
    <body style="font-family: Arial; margin: 40px;">
        <h2>Resultado de {notas['Nombre']}</h2>
        <table border="1" cellpadding="6" style="border-collapse: collapse;">
            <tr><th>Asignatura</th><th>Nota</th></tr>
            <tr><td>Matemáticas</td><td>{notas['Matemáticas']}</td></tr>
            <tr><td>Lenguaje</td><td>{notas['Lenguaje']}</td></tr>
            <tr><td>Ciencias</td><td>{notas['Ciencias']}</td></tr>
            <tr><td>Historia</td><td>{notas['Historia']}</td></tr>
            <tr><td>Inglés</td><td>{notas['Inglés']}</td></tr>
        </table>
        <h3>Promedio general: {round(promedio, 2)}</h3>
        <img src="{ruta_img}" alt="Gráfica de notas" width="500">
    </body>
    </html>
    """
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)

    print("Archivo resultado.html creado correctamente")