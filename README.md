# TP0 Tests Automatizados

## Setup

Instalar paquetes requeridos (recomendamos usar pyenv or virtualenv)

```
pip install -r requirements.txt
```

## Ejecución

Ejecutar `pytest`, pasando la ruta al repositorio como variable de entorno.
La ruta no es una URL de github, sino la ruta absoluta al repositorio en tu sistema de archivos.

```
REPO_PATH=/path/to/repo pytest
```

Tambien, podemos ver todos los logs al ejecutar los tests con la flag `-s`.

```
REPO_PATH=/path/to/repo pytest -s
```

### ADVERTENCIAS:

- Antes de cada test se detienen y eliminan todos los contenedores, imágenes y redes. Asegúrate de no tener contenedores importantes corriendo en tu sistema.

- Antes de cada test se resetea la rama actual y se cambia a la rama a verificar, lo que eliminará cambios sin commitear.
