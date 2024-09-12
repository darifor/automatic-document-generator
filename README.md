# Generador automático de documentos

[python](https://img.shields.io/badge/python-brightgreen?style=for-the-badge&logo=python&labelColor=black)

Imagina que eres profesor universitario. En una tabla de excel almacenas las notas de tus alumnos para cada
asignatura. Se acercan las navidades y debes informar a cada uno de sus resultados académicos. Te tocará consultar tu archivo de excel, seleccionar las notas de cada asignatura por alumno y redactar un 
documento de word para cada uno de ellos en el que presentes toda la información. Una tarea de chinos, vaya. 

No sufras más. Con esta aplicación sólo tendrás que hacer un click y el sistema hará todo el trabajo por ti en 
un abrir y cerrar de ojos. Lo único que debes hacer es asegurarte de que la carpeta *"comunicados"*, el excel
*"alumnos.xlsx"* con las notas del alumnado y el documento *"plantilla.docx"* con el modelo de carta que deseas
enviar estén en el mismo directorio que la alicación "automatizar_word.py". 

## Componentes del sistema

1. **comunicados** &rarr; directorio en el que se almacenan los archivos de texto de cada alumno, generados por el sistema.
2. **alumnos.xlsx** &rarr; archivo de excel en el que se recogen las notas de cada alumno para cada asignatura.
3. **plantilla.docx** &rarr; modelo de archivo de texto que se desea generar.
4. **automatizar_word.py** &rarr; aplicación.
