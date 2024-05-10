
# Leer y escribir archivos
archivo = open("ejemplo.txt", "w")
archivo.write("¡Hola, Python!")
archivo.close()

archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Listas
frutas = ["manzana", "plátano", "naranja"]
print(frutas)

# Acceder a un elemento de la lista
print(frutas[0])

# Agregar un elemento a la lista
frutas.append("pera")
print(frutas)

# Longitud de la lista
print(len(frutas))