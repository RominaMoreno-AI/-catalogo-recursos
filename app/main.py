"""
Catálogo de recursos académicos
--------------------------------
Punto de entrada de la aplicación. Por ahora solo identifica el proyecto;
la lógica de registro y consulta de recursos se implementará en una
versión futura (ver docs/alcance.md).
"""

from configuracion import NOMBRE_PROYECTO, VERSION


def main():
    print(f"{NOMBRE_PROYECTO} - versión {VERSION}")
    print("Estructura inicial del proyecto lista.")


if __name__ == "__main__":
    main()
