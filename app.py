import sys

def modificar_archivo(ruta_archivo):
    try:
        # Abrir el archivo en modo de escritura
        with open(ruta_archivo, 'a') as archivo:
            # Agregar el texto "Hola mundo" al final del archivo
            archivo.write("Hola mundo\n")
        print("Archivo modificado con éxito.")
    except Exception as e:
        print("Ocurrió un error al modificar el archivo:", e)

if __name__ == "__main__":
    # Verificar que se proporcionó la ruta del archivo como argumento
    if len(sys.argv) < 2:
        print("Por favor, proporciona la ruta del archivo como argumento.")
        sys.exit(1)

    # Obtener la ruta del archivo desde los argumentos de línea de comandos
    ruta_archivo = sys.argv[1]

    # Llamar a la función para modificar el archivo
    modificar_archivo(ruta_archivo)
