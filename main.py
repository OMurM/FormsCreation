from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

productos = [
    Producto("Llibre A", "Educació", 12.5),
    Producto("Llibre B", "Literatura", 9.0),
    Producto("Llibre C", "Educació", 15.0),
    Producto("Llibre D", "Ficció", 8.5)
]

def crear_informe(pdf_filename, productos):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    espacio_superior = 100
    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.blue)
    c.drawString(100, 780 - espacio_superior, "Monlau la Sagrera")
    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.black)
    c.drawString(100, 760 - espacio_superior, "Informe de Productes - DAM2")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 740 - espacio_superior, "Oscar Mur Matutano")
    
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    c.setFont("Helvetica", 10)
    c.drawString(450, 740 - espacio_superior, f"Data: {fecha_actual}")
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(100, 700 - espacio_superior, "Nom")
    c.drawString(200, 700 - espacio_superior, "Categoria")
    c.drawString(350, 700 - espacio_superior, "Preu (€)")

    c.setFont("Helvetica", 10)
    y_position = 680 - espacio_superior
    for producto in productos:
        c.drawString(100, y_position, producto.nombre)
        c.drawString(200, y_position, producto.categoria)
        c.drawString(350, y_position, f"{producto.precio:.2f} €")
        y_position -= 20

        if y_position < 100:
            c.showPage()  
            c.setFont("Helvetica-Bold", 12)
            c.drawString(100, 700, "Nom")
            c.drawString(200, 700, "Categoria")
            c.drawString(350, 700, "Preu (€)")
            y_position = 680 
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.grey)
    c.drawString(100, 50, "Generat automàticament.")
    
    c.save()

crear_informe("informe_productos.pdf", productos)
