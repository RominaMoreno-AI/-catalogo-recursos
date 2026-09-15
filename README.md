# Catálogo de recursos académicos

## Descripción

Proyecto desarrollado para la materia **Desarrollo de Aplicaciones y
Servicios Virtuales** (Universidad Iberoamericana León). Representa la
estructura inicial de un sistema que, en versiones futuras, permitirá
registrar y consultar recursos académicos como libros, sitios web, videos,
artículos y herramientas de software.

## Objetivo

Aplicar de manera autónoma el flujo de preparación, versionamiento y
colaboración de un proyecto utilizando Visual Studio Code, Python, Git y
GitHub.

## Estructura general

```
catalogo_recursos/
├── app/
│   ├── main.py
│   └── configuracion.py
├── data/
│   └── recursos.json
├── docs/
│   ├── alcance.md
│   ├── criterios.md
│   ├── respuestas.md
│   └── evidencias/
├── tests/
│   └── test_basico.py
├── .gitignore
├── README.md
├── requirements.txt
└── CHANGELOG.md
```

## Tecnologías utilizadas

- Python 3.12
- Git y GitHub (control de versiones y colaboración)
- Visual Studio Code
- Bibliotecas: `requests`, `rich`

## Preparar el entorno

1. Clona o descarga el repositorio.
2. Crea un entorno virtual:
   ```
   python -m venv .venv
   ```
3. Actívalo:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Ejecuta la aplicación:
   ```
   python app/main.py
   ```

## Dependencias

Ver `requirements.txt`:

- `requests`
- `rich`

## Próximas mejoras

- Implementar el registro y la consulta de recursos descritos en
  `docs/alcance.md`.
- Agregar validación de datos al crear nuevos recursos.
- Incorporar pruebas automatizadas adicionales en `tests/`.
- Integrar la biblioteca `requests` para consultar fuentes académicas
  externas.
- Mejorar la salida en consola utilizando `rich` para tablas y mensajes.
## Tipos de recursos

- Artículos académicos
- Libros
- Cursos en línea
- Documentación técnica
- Tutoriales