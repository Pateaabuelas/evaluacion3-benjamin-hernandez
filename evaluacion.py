import csv
# Función para agregar productos al inventario
def agregar_producto():
    # Solicitar al usuario que ingrese los datos del producto
    ID = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto (Electrónica, Textil o Calzado): ")
    precio = input("Ingrese el precio del producto: ")
    
    # Abrir el archivo CSV en modo de escritura
    with open('inventario.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Escribir los datos del producto en el archivo CSV
        writer.writerow([id, nombre, categoria, precio])
    
    print("Producto agregado al inventario.")
    print("---------------------------------")

# Función para leer el inventario
def leer_inventario():
    # Abrir el archivo CSV en modo de lectura
    with open('inventario.csv', 'r') as file:
        reader = csv.reader(file)
        
        # Leer y mostrar todos los productos almacenados en el archivo
        for row in reader:
            print("ID:", row[0])
            print("Nombre:", row[1])
            print("Categoría:", row[2])
            print("Precio:", row[3])
            print("---------------------------------")

# Función para clasificar los productos y generar un archivo de texto
def clasificar_productos():
    # Crear listas para cada categoría
    electronica = []
    textil = []
    calzado = []
    
    # Abrir el archivo CSV en modo de lectura
    with open('inventario.csv', 'r') as file:
        reader = csv.reader(file)
        
        # Leer y clasificar los productos en las listas correspondientes
        for row in reader:
            if row[2] == "Electrónica":
                electronica.append(row)
            elif row[2] == "Textil":
                textil.append(row)
            elif row[2] == "Calzado":
                calzado.append(row)
    
    # Generar el archivo de texto con la clasificación de productos
    with open('clasificacion_productos.txt', 'w') as file:
        file.write("Electrónica:\n")
        for producto in electronica:
            file.write(", ".join(producto) + "\n")
        
        file.write("\nTextil:\n")
        for producto in textil:
            file.write(", ".join(producto) + "\n")
        
        file.write("\nCalzado:\n")
        for producto in calzado:
            file.write(", ".join(producto) + "\n")
    
    print("Productos clasificados y archivo de texto generado.")
    print("---------------------------------")

# Función principal del programa
def main():
    while True:
        # Mostrar el menú de opciones
        print("------ MENÚ ------")
        print("1. Agregar producto al inventario")
        print("2. Leer el inventario")
        print("3. Clasificar productos y generar archivo de texto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            leer_inventario()
        elif opcion == "3":
            clasificar_productos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        print()

# Ejecutar el programa
if __name__ == "__main__":
    main()
