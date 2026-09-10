"""
Prueba básica para verificar que el proyecto está correctamente
estructurado y que la configuración se puede importar.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from configuracion import NOMBRE_PROYECTO, RUTA_DATOS  # noqa: E402


def test_nombre_proyecto():
    assert NOMBRE_PROYECTO == "Catálogo de recursos académicos"


def test_recursos_json_existe_y_es_lista():
    ruta = os.path.join(os.path.dirname(__file__), "..", RUTA_DATOS)
    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)
    assert isinstance(datos, list)
    assert len(datos) >= 2
