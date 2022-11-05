import pytesseract
from pytesseract import Output
from PIL import Image
import csv
import os
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Enseñarle al python dónde se encuentra teserract

"""" Todo lo que está acá arriba son los paquetes necesarios para que el programa funcione """

#           Estas son las variables globales           #

celulares = "" # Guarda una cadena con todos los números de celulares
usuarios = "" # Guarda una cadena con todos los nombres de usuarios
index_img = 1  # Es el índice de los archivos de imágenes
temp_cel = 0 # Un contador para los celulares de cada captura
temp_usr = 0 # Un contador para los usuarios de cada captura
caracteres_invalidos = [',','.','=','!'] # Autodescriptivo

#           Estas son las variables globales           #

def WriteContacts():
    global celulares
    global usuarios
    global temp_cel
    global temp_usr

    """ </> Convertir textos en listas </> """

    celulares = celulares[:-1]
    celulares = celulares.split(',')
    usuarios = usuarios[:-1]
    usuarios = usuarios.split(',')

    """ </> Convertir textos en listas </> """

    """ Escribir Contactos """

    columnas = ['Nombres', 'Celulares'] # Se definen las columnas del csv
    with open ('contactos.csv', 'w', newline='') as f: # Abrir el archivo y definir algunos parámetros
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerow(columnas) # Se escriben las columnas del csv

        if len(usuarios) == len(celulares):
            for w in range(len(celulares)):
                write.writerow([usuarios[w],celulares[w]])
        else:
            print('Aquí hubo un error...')

    print('Número de elementos [Números: '+(str(len(celulares)))+"]")
    print('Número de elementos [Usuarios: '+(str(len(usuarios)))+"]")

    """ Escribir Contactos """

def ImgScan():
    global celulares
    global usuarios
    global index_img
    global temp_cel
    global temp_usr

    """ </> Comprobar si existen capturas para analizar </> """
    if os.path.exists(str(index_img)+".png") == True :
        img = Image.open(str(index_img)+'.png') # Existe una captura, se procede a abrirla
        print('######## Datos imagen: '+str(index_img)+" ########")
        index_img = index_img+1
    elif os.path.exists(str(index_img)+".jpg") == True:
        img = Image.open(str(index_img)+'.jpg') # Existe una captura, se procede a abrirla
        print('######## Datos imagen: '+str(index_img)+" ########")
        index_img = index_img+1
    else:
        input('Se terminaron las capturas')
        WriteContacts()
        quit()
        """ </> Aquí se termina el bloque </> """

    datos = pytesseract.image_to_data(img, lang="spa+eng", output_type=Output.DICT) # Se convierte la captura en textos
    n_boxes = len(datos['level']) # Guarda la cantidad de elementos (Palabras) en una variable

    for i in range(n_boxes):

        x, y, text = (datos['left'][i], datos['top'][i], datos['text'][i])
        if text != "" or text != " " or text != "  " or text != "   ":

            """ Bloque para filtrar números de celular """
            if text.isdigit() == True: # Si el texto es un dato numérico entonces...
                if len(text) == 10: # Se comprueba si el número tiene 10 dígitos (Se cuenta del 0 al 10)

                    if text in celulares: # Si el número ya existe dentro de la variable celulares...
                        pass # Se descarta
                    else:
                        temp_cel = temp_cel+1
                        print(text)
                        celulares = celulares+text+","
                else: # Si no tiene 10 dígitos
                     pass # Se descarta
            elif text.startswith('@') == True and len(text) >= 7 and len(text) <= 25: # Si parece ser un nombre de usuario...
                text = text.translate(str.maketrans('','',''.join(caracteres_invalidos)))#ELiminar caracteres inválidos
                usuarios = usuarios+text+"," #  Se guarda directo, al ser una imagen estática no se necesita depurar tantos errores
                print(text+"\n")
                temp_usr = temp_usr+1
            else: # Si no ? (Qué raro)
                pass # Se descarta
    if temp_cel < temp_usr:
        print('### ¡Captura conflictiva: Encontré más usuarios que números! ###')
    elif temp_cel > temp_usr:
        print('### ¡Captura conflictiva: Encontré más números que usuarios! ###')
    else:
        pass
    temp_cel = 0
    temp_usr = 0

while True:
    ImgScan()
