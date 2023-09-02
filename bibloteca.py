import libro as l

def ejemplares_prestados():
    for libro in l.libros:
        print(f"El libro '{libro['titulo']}' posee la cantidad de: {libro['cant_ej_pr']} en préstamo") if libro['cant_ej_pr'] > 0 else print(f"El libro '{libro['titulo']}' no posee ejemplares prestados")
    
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    return None

def eliminar_ejemplar_libro():
    libro_registrado = False
    op = input("Ingrese el código del libro: ")
    for libro in l.libros:
        if libro['cod'] == op:
            libro_registrado = True
            if libro['cant_ej_ad'] > 0:
                libro['cant_ej_ad'] -= 1
                return print(f"Se ha eliminado exitosamente un ejemplar del libro '{libro['titulo']}'")    
            else:
                return print(f"El libro '{libro['titulo']}' no posee ejemplares en circulación")   
    if libro_registrado == False:            
        return print("ERROR: El código ingresado no esta registrado")     

def prestar_ejemplar_libro():  
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
                    if prestamo_sino in ('SI','NO'):
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
                    if devuelve_libro in ('SI','NO'):
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
    return None