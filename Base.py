#clase principal para la descripcion
class Descripcion:
    def __init__(self, iniciador, descripcion):
        self.iniciador = iniciador
        self.descripcion = descripcion
    def __str__(self):
        return f"{self.iniciador},{self.descripcion}"

#esta funcion sirve para escribir las lineas
def convertir_escribir(datos,numero):
    numero = (f"{numero}")
    with open ("descripcion\\"+numero+".txt", "w", encoding="UTF-8") as escribir:
        escribir.write(datos)   

#esta funcion crea la descripcion y la persona 
def crear():
    cantidad = input("¿Cuantas imagenes vas a clasificar?")
    try:
        cantidad = int(cantidad)
        numero = 1
        iniciador = input("cual es tu iniciador")
        for i in range(cantidad):
            descripcion = input(f"Escribe la descripcion de la imagen #{numero}")
            #nos la guarda con un valor
            i = Descripcion(iniciador," " +descripcion)
            #ahora le digo que lance la funcion de editar
            datos = (f"{i}")
            convertir_escribir(datos,numero)
            numero+=1    
        print("Las descripciones han sido creadas con exito")    
    except:
        print(f"{cantidad} no es un numero valido de imagenes, intenta de nuevo")
        crear()
        
#leer la descripciones  
def leer(cual):
    with open ("descripcion\\"+cual+".txt",encoding="UTF-8") as descripcion:
        lineas= descripcion.readlines()
        print (lineas)
              
#esta es la interfaz
def interfaz():
    hacer = input("¿Que deseas hacer? 1 = Crear descripciones. 2 = Ver descripciones. Otro = Cerrar")
    if hacer == "1":
        crear()
        interfaz()
    elif hacer == "2":
        cual = input ("Escribe el numero de la imagen que deseas ver su descripcion")
        try:
            leer(cual)
        except:
            print("Esa imgen no existe")
        interfaz()
    else:
        print("Gracias por usar")

        
#lanzamos el programa
interfaz()