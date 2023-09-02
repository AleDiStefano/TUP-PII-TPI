import libro as l

"""
# Crear una lista vacía para almacenar los libros

libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
"""
def ejemplares_prestados():
    
    #Creamos una bandera para validar que el libro exista en la lista
    libro_registrado = False
    
    op = input("Ingrese el código del libro: ")
    for libro in l.libros:
        if libro['cod'] == op:
            libro_registrado = True
            
            #Creamos una variable para no tener que hacer la cuenta en cada print de pantalla
            cant_disp = libro['cant_ej_ad'] - libro['cant_ej_pr']
            if cant_disp > 0:
                print(f"Se encuentran disponible {cant_disp} unidad/es del libro {libro['titulo']} del autor {libro['autor']}")
                while True:
                    prestamo_sino = str(input("¿Desea confirmar el préstamo? (SI/NO): "))
                    prestamo_sino = prestamo_sino.upper()
                    if prestamo_sino == 'SI' or prestamo_sino == 'NO':
                        break
                    else:
                        print("Opción inválida")
                
                if prestamo_sino == 'SI':
                    libro['cant_ej_pr'] += 1
                    return print(f"Préstamo exitoso, cantidad de ejemplares prestados acutalizada a: {libro['cant_ej_pr']}")
            else:
                print(f"No se encuentran disponibles para prestar unidades del libro {libro['titulo']} del autor {libro['autor']}")
            
    if libro_registrado == False:            
        return print("ERROR: El código ingresado no esta registrado")        
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    #completar
    return None

def devolver_ejemplar_libro():
    libro_registrado = False
    
    op = input("Ingrese el código del libro: ")
    
    for libro in l.libros:
        if libro['cod'] == op:
            libro_registrado = True
            
            if libro['cant_ej_pr'] > 0:
                while True:
                    devuelve_libro = str(input("¿Desea confirmar la devolucion? (SI/NO): "))
                    devuelve_libro = devuelve_libro.upper()
                    if devuelve_libro == 'SI' or devuelve_libro == 'NO':
                        break
                    else:
                        print("Opción inválida")
                        
                if devuelve_libro == 'SI':
                    libro['cant_ej_pr'] -= 1
                    return print(f"Devolucion exitosa, cantidad de ejemplares prestados acutalizada a: {libro['cant_ej_pr']}")
            else:
                print("Error: no se encuentran libros prestados")
                        
    if libro_registrado == False:            
        return print("ERROR: El código ingresado no esta registrado") 

def nuevo_libro():
    #completar
    return None

