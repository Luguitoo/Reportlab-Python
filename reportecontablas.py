#Librerias
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

# Crear PDF, nombre y dimensiones del reporte
pdf = SimpleDocTemplate(
    "reporte.pdf",
    pagesize=A4,
    rightMargin=inch,
    leftMargin=inch,
    topMargin=inch,
    bottomMargin=inch/2
)
Story = []
# Estilos
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
# Cabecera
text = '''
    <strong><font size=14>Alumnos Matriculados en {a}.</font></strong>
'''.format(a = "Quimica")
text2 = '''
    <strong><font size=10>Profesor: {a}</font></strong>
'''.format(a = "Carlos Lugo")
text3 = '''
    <strong><font size=10>Curso: {a}</font></strong>
'''.format(a = "Primer Curso, Sociales")
#Datos o registros, esto esta exagerado para testeo.
alumnos = ["Carlos Lugo Zacarias", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Hernesto Mauricio Gimenez Atencio", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"]
puntajes = [5, 10, 10,5,5,5,10,10,5,5,5,10,10,5,5,5,10,10,5,5,5,10,10,5,5,5,10,10,5,5,5,10,10,5,5, 5,10,10,5,5,5,10,10,5,5,5,10,10,5,5]
#Adjuntamos los titulos declarados mas arriba, osea las cabeceras
Story.append(Paragraph(text2))
Story.append(Paragraph(text3))
Story.append(Paragraph(text, styles['Center']))
Story.append(Spacer(1, 20))
#Declaramos los datos de la cabecera de la tabla, los titulos y tambien sus estilos
data = [(
    Paragraph('<strong><font size=6>#</font></strong>', styles['Center']),
    Paragraph('<strong><font size=6>Nombre y Apellido</font></strong>', styles['Center']),
    Paragraph('<strong><font size=6>P.Etapa PT:</font></strong>', styles['Center']),
    Paragraph('<strong><font size=6>Calificación</font></strong>', styles['Center']),
    Paragraph('<strong><font size=6>S.Etapa PT:</font></strong>', styles['Center']),
    Paragraph('<strong><font size=6>Calificación</font></strong>', styles['Center'])
)]
#Aqui acomplamos los registros o datos a nuestra tabla data, estos seran los datos mostrados de bajo de los headers
for x in range(0, len(alumnos)):
    count = str(x + 1)
    cal = "Sin calificacion"
    data.append((
        Paragraph('<font size=6>%s</font>' % count, styles['Normal']),
        Paragraph('<font size=6>%s</font>' % alumnos[x], styles['Normal']),
        Paragraph('<font size=6>%s</font>' % puntajes[x], styles['Normal']),
        Paragraph('<font size=6>%s</font>' % cal, styles['Normal']),
        Paragraph('<font size=6>%s</font>' % puntajes[x], styles['Normal']),
        Paragraph('<font size=6>%s</font>' % cal, styles['Normal'])
    ))
 #Declaramamos que la tabla recibira como dato los datos anteriores y le damos la dimensiones a cada uno de nuestros campos
table = Table(
    data,
    colWidths=[20,120,50,60,50,60]
)
table.setStyle(
    TableStyle([
        ('VALIGN',(0, 0), (-1, -1),'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ])
)
Story.append(table)
pdf.build(Story)