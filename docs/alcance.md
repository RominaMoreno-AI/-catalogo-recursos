# Alcance del proyecto

Este documento describe lo que podría hacer una versión futura del sistema
**Catálogo de recursos académicos**. La versión actual únicamente prepara la
estructura de archivos y documentación; ninguna de las funcionalidades
descritas aquí está implementada todavía.

## Funcionalidades futuras propuestas

1. **Registro de recursos**: permitir agregar libros, sitios web, videos,
   artículos y herramientas de software a `data/recursos.json` desde una
   interfaz de línea de comandos o una API.
2. **Consulta y filtrado**: buscar recursos por tipo, tema, nivel o autor,
   devolviendo resultados ordenados y paginados.
3. **Validación de datos**: verificar que cada recurso nuevo cumpla con un
   esquema mínimo (campos obligatorios, tipos de dato correctos) antes de
   almacenarlo.
4. **Exportación de reportes**: generar resúmenes en formato Markdown o CSV
   con estadísticas del catálogo (por ejemplo, cantidad de recursos por
   tema o por nivel).
5. **Integración con fuentes externas**: usar la biblioteca `requests` para
   consultar APIs públicas (repositorios académicos, bibliotecas digitales)
   y sugerir recursos adicionales.
6. **Interfaz enriquecida en consola**: usar la biblioteca `rich` para
   mostrar tablas y mensajes con mejor formato al listar o buscar recursos.
