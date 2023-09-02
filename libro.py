import cod_generator as c

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS',
          'cant_ej_ad': 3,
          'cant_ej_pr': 1,
          "titulo": "Cien años de soledad",
          "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c',
          'cant_ej_ad': 4,
          'cant_ej_pr': 2,
          "titulo": "El principito",
          "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE',
          'cant_ej_ad': 1,
          'cant_ej_pr': 0,
          "titulo": "El código Da Vinci",
          "autor": "Dan Brown"}

#Se crea una lista con cada libro para poder iterar
libros = [libro1,libro2,libro3]

def nuevo_libro():
    titulo = input("Ingrese el titulo del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridas: "))
    cod = generar_codigo()
    nuevo_libro = {
        'cod': cod,
        'cant_ej_ad': cant_ej_ad,
        'cant_ej_pr': 0,
        "titulo": titulo,
        "autor": autor
    }
    libros.append(nuevo_libro)
    print(f"El libro {titulo} del autor {autor} se agregado con exito, con la cantidad de ejemplares: {cant_ej_ad} y con el código: {cod}")

def generar_codigo():
    cod = c.generar()
    return cod