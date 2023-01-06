#Librerias
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#Datos o registros
alumnos = ["Carlos Lugo Zacarias", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Hernesto Mauricio Gimenez Atencio", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"
           ,"Carlos Manolo Piris Delgado", "Mathias Ortellado", "Anibal Lopez", "Cristiano Ronaldo", "Lionel Messi"]
puntajes = [5, 10, 10,5,5,5,10,10,5,5,5,10,10,5,5]
pt = 10
#Dando formato al pdf, letter = A4
canvas = canvas.Canvas("form.pdf", pagesize=letter)
#Grosor de la linea
canvas.setLineWidth(.3)
#Fuente que se va a utilizar en el pdf
canvas.setFont('Helvetica', 12)
#El primer parametro es el margen osea x, el segundo es la altura osea y, el tercero ya seria el texto
canvas.drawString(30,750,'COLEGIO NACIONAL HEROES DEL CHACO')
#15 pixeles menos es un salto de linea
canvas.drawString(30,735,'Profesor:')
canvas.drawString(400,735,"{nombre}, {apellido}".format(nombre="Carlos Gabriel",apellido="Lugo Zacarias"))
#Dibuja la linea
canvas.line(400,733,600,733)
#Parte del Reporte
canvas.drawString(30,705,'Alumnos Matriculados en {materia}:'.format(materia = "Quimica"))
#Headers
canvas.drawString(50,690, 'Nombres y Apellidos')
canvas.drawString(220,690, 'P.Etapa PT: {a}'.format(a = pt))
canvas.drawString(310,690, 'Calificación')
canvas.drawString(390,690, 'S.Etapa PT: {a}'.format(a = pt))
canvas.drawString(480,690, 'Calificación')
total = 690
#Ya hacemos los reportes uno por uno con un for, y dandole a total -15, osea un salto de linea.
for x in range(0, len(alumnos)):
    canvas.drawString(30,total - 15, "{a}.".format(a = x +1))
    canvas.drawString(50,total - 15, "{a}".format(a = alumnos[x]))
    canvas.drawString(250,total - 15,"{a}".format(a=puntajes[x]))
    canvas.drawString(320, total - 15, "{a}".format(a="Aun no"))
    canvas.drawString(420, total - 15, "{a}".format(a=puntajes[x]))
    canvas.drawString(490, total - 15, "{a}".format(a="Aun no"))
    total -= 15

canvas.save()