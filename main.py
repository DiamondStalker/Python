import json
import os
def borrarPantalla():
  #Para Unix/Linux/MacOS/BSD
  if os.name == "posix":
    os.system ("clear")
  
  #Para DOS/Windows
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")


def Archivo():
  with open('Libreria.json') as f:
    Libreria = json.load(f)
  return Libreria

def Cuantos_libros():
  borrarPantalla()
  Libreria = Archivo()
  
  libros = Libreria["bookstore"]["book"]
  
  print (f"\n      Existen {len(libros)} libros")
  input ("      Presiona ENTER para continuar....")

def Mostrar_titulo_autor():
  borrarPantalla()
  Libreria = Archivo()
  
  listalibros = Libreria["bookstore"]["book"]

  x = 0

  while x < len(listalibros):
    Datos = Libreria["bookstore"]["book"][x]

    print("------------")
    print ("Titulo del libro : ",Datos["title"]["__text"],"\n Autor / autores : ",Datos["author"])
    x += 1
  input ("      Presiona ENTER para continuar....")

def Buscar_libro():
  borrarPantalla()
  Libreria = Archivo()

  Nombre = input ("       Ingresa el nombre de libro a buscar en la liberia\n")

  Nombre = Nombre.lower()

  listalibros = Libreria["bookstore"]["book"]

  x = 0

  while x < len(listalibros):

    Titulo = Libreria["bookstore"]["book"][x]["title"]["__text"].lower()

    Comparacion = Titulo.find(Nombre)

    if Comparacion >= 0:
      print (f" El libro que empieza o que tenga el nombre {Nombre} se encuentra en la libreria")
      print (Libreria["bookstore"]["book"][x]["title"]["__text"])
      break
    else: x+=1
  
  if x == len(listalibros): print (f"      El libro {Nombre} no se encuentra dentro de la libreria")
  input ("      Presiona ENTER para continuar....")


def Precios():
  Libreria = Archivo()
  borrarPantalla()

  PrecioMenor = float(input("Ingrese el precio menor  "))
  PrecioMayor = float(input("Ingrese el precio menor  "))

  listalibros = Libreria["bookstore"]["book"]

  x = 0

  while x < len(listalibros):
    PrecioLibro = float(listalibros[x]["price"])
    if PrecioMenor <=PrecioLibro and PrecioMayor >= PrecioLibro: 
      print(listalibros[x]["title"]["__text"],"-",listalibros[x]["price"])
    x += 1
  input ("      Presiona ENTER para continuar....")

opc = 1

while opc != 0:
  borrarPantalla()
  print("\n Menu\n 1. Cuantos libros existen\n 2. Mostrar todos los libros y autores\n 3. Buscar libro\n 4. Rango precios")

  opc = int(input("\n Ingresa la opcion "))

  if opc == 1: Cuantos_libros()
  if opc == 2:Mostrar_titulo_autor()
  if opc == 3:Buscar_libro()
  if opc == 4:Precios()