# Respuestas

## Pregunta de control — Sección 6 (Instalar dependencias)

**¿Qué ventaja tiene registrar las dependencias del proyecto en
requirements.txt en lugar de compartir la carpeta .venv?**

`requirements.txt` es un archivo de texto ligero que solo indica los
nombres y versiones de las bibliotecas necesarias, mientras que `.venv/`
contiene miles de archivos binarios y depende del sistema operativo y de
la versión de Python con la que fue creado. Compartir `.venv/` haría el
repositorio pesado, no portable entre sistemas operativos y difícil de
versionar. En cambio, cualquier persona puede recrear un entorno idéntico
en su propia máquina ejecutando `pip install -r requirements.txt`, sin
importar su sistema operativo.

## Pregunta de control — Sección 12 (Iniciar colaboración)

**¿Por qué el repositorio que tienes ahora en tu computadora no es el
mismo concepto que el fork creado en GitHub?**

El **fork** es una copia completa del repositorio original alojada en la
cuenta de GitHub de la persona colaboradora; sigue siendo un repositorio
remoto en la nube. El repositorio que queda en la computadora después de
hacer `clone` es una **copia local** de ese fork, con su propio historial
descargado y con un remoto (`origin`) apuntando al fork en GitHub. Son
tres repositorios distintos relacionados entre sí: el original, el fork
(remoto) y la copia local del fork; los cambios solo se sincronizan entre
ellos cuando se hace `push`, `pull` o `fetch`.

---

## Preguntas individuales

**79. ¿Cómo identificaste el comando necesario cuando la práctica no lo
proporcionó?**

A partir de la acción descrita (por ejemplo, "convierte la carpeta en un
repositorio Git" o "consulta el estado del repositorio") identifiqué el
verbo clave de la operación (inicializar, consultar, preparar, registrar,
relacionar, publicar) y lo relacioné con el comando de Git que realiza
exactamente esa función, apoyándome en `git help <comando>` o en la ayuda
integrada de Visual Studio Code cuando tuve dudas, y verificando siempre
el resultado con un comando de consulta (`git status`, `git log`, `git
branch`, etc.) antes de continuar.

**80. ¿Qué diferencia existe entre preparar un archivo para un commit y
crear el commit?**

Preparar un archivo (`git add`) lo mueve al **área de preparación
(staging area)**, es decir, lo marca como candidato para el próximo
registro de cambios, pero todavía no queda guardado en el historial.
Crear el commit (`git commit`) toma todo lo que está en el área de
preparación y lo guarda de forma permanente en el historial del
repositorio, junto con un mensaje que describe el cambio.

**81. ¿Cómo puedes comprobar en qué rama estás trabajando?**

Con `git branch` (la rama activa aparece marcada con un asterisco) o con
`git status`, que muestra el nombre de la rama actual en la primera
línea.

**82. ¿Cómo puedes determinar qué archivos fueron modificados antes de
registrarlos?**

Con `git status`, que lista los archivos modificados, los nuevos (sin
seguimiento) y los que ya están preparados para el commit, diferenciando
cada categoría.

**83. ¿Cómo puedes observar exactamente qué cambió dentro de un
archivo?**

Con `git diff` para ver los cambios que aún no están preparados, o
`git diff --staged` para ver los cambios ya agregados al área de
preparación. Ambos muestran línea por línea qué se agregó y qué se
eliminó.

**84. ¿Por qué debe reconstruirse .venv después de obtener un
repositorio?**

Porque `.venv/` está excluida del repositorio mediante `.gitignore` y
nunca se sube a GitHub: es un entorno local que depende del sistema
operativo y de la ruta absoluta de la máquina donde se creó, por lo que
no sería funcional si se compartiera directamente. Cada persona debe
crear su propio entorno virtual y luego instalar las dependencias
indicadas en `requirements.txt` para tener un entorno equivalente.

**85. ¿Qué relación existe entre requirements.txt y .gitignore?**

Son complementarios: `.gitignore` evita que el entorno virtual `.venv/`
(pesado y no portable) se suba al repositorio, mientras que
`requirements.txt` sí se versiona y permite reconstruir ese mismo entorno
en cualquier máquina. Uno excluye lo que no debe compartirse y el otro
documenta lo necesario para recrearlo.

**86. ¿Por qué la colaboración se realiza desde una rama y no
directamente desde main?**

Trabajar en una rama independiente permite realizar y probar cambios sin
afectar el código estable que está en `main`. Esto facilita la revisión
mediante un Pull Request antes de integrar los cambios, evita conflictos
si varias personas trabajan al mismo tiempo, y permite descartar una
rama sin consecuencias si el cambio no resulta adecuado.

**87. ¿Por qué una solicitud de cambios no requiere crear un Pull Request
nuevo?**

Porque un Pull Request está vinculado a una rama específica, no a un
commit en particular. Al hacer `push` de nuevos commits a esa misma rama
remota, GitHub actualiza automáticamente el Pull Request ya existente
con los cambios más recientes, permitiendo que la persona revisora vea
la actualización sin necesidad de abrir una nueva solicitud.

**88. Después de realizar el merge en GitHub, ¿por qué todavía es
necesario actualizar el repositorio local?**

Porque el merge ocurre en el repositorio remoto (en GitHub), pero el
repositorio local de la persona propietaria no se actualiza
automáticamente. Es necesario ejecutar `git pull` (o `git fetch` seguido
de `git merge`) sobre la rama principal local para descargar e integrar
los cambios que ya existen en el remoto y que la copia local aún no
tiene.
