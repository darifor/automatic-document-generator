import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate("plantilla.docx")
nombre = "Daniel Ribes"
telefono = "91 544 34 20"
correo = "mikelson@gmx.es"
fecha = datetime.today().strftime("%d/%m/%Y")

constantes = {'nombre': nombre,
              'telefono': telefono,
              'correo': correo,
              'fecha': fecha}

df = pd.read_excel("alumnos.xlsx")

for indice, fila in df.iterrows():
    contenido = {'nombre_alumno':fila['nombre_alumno'],
                 'nota_mat':fila['mat'],
                 'nota_fisica':fila['fisica'],
                 'nota_quimica':fila['quimica']}
    contenido.update(constantes)
    doc.render(contenido)
    doc.save(f"comunicados/notas_de_{fila['nombre_alumno']}.docx")
