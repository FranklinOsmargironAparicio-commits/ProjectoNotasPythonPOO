# Registro y Visualización de Notas

Proyecto para **registrar notas de un estudiante** desde una página web, guardarlas en un archivo JSON y generar un **reporte HTML con gráfica de barras** usando Python.

---

## Características

- Formulario en HTML para ingresar nombre y notas  
- Guardado en JSON directamente desde el navegador  
- Procesamiento en Python para calcular el promedio  
- Reporte HTML con tabla de notas, promedio y gráfica  

---

## Estructura del Proyecto

```
.
├── index.html          → Formulario para capturar notas
├── notas.json          → Archivo generado con los datos
├── procesar_notas.py   → Script de Python para procesar
├── grafica.png         → Imagen con la gráfica de barras
└── resultado.html      → Reporte final con tabla y gráfico
```

---

## Requisitos

- Navegador moderno (Chrome o Edge recomendado)  
- Python 3.8 o superior  
- Librerías: pandas, matplotlib  

Instalación de dependencias:  
```
pip install pandas matplotlib
```

---

## Uso

1. **Abrir el formulario**  
   - Ejecuta `index.html` en el navegador  
   - Ingresa el nombre y las notas  
   - Guarda el archivo como `notas.json`  

2. **Procesar los datos**  
   - Ejecuta el script de Python en la misma carpeta:  
     ```
     python procesar_notas.py
     ```
   - Se generarán `grafica.png` y `resultado.html`  

3. **Visualizar el reporte**  
   - Abre `resultado.html` en tu navegador  

---

## Formato del JSON

Ejemplo de archivo generado:

```
{
  "Nombre": "Ana Pérez",
  "Matemáticas": 8.5,
  "Lenguaje": 7.9,
  "Ciencias": 9.2,
  "Historia": 8.0,
  "Inglés": 8.7
}
```

---

## Problemas Comunes

- El navegador no guarda el archivo → Usa Chrome o Edge  
- Promedio muestra NaN → Alguna nota no es numérica  
- No encuentra `notas.json` → Asegúrate de que esté en la misma carpeta que el script  

---

## Licencia

Este proyecto está bajo la **Licencia MIT**.  
Puedes usarlo, modificarlo y compartirlo libremente.  
