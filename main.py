#Esto se ejecuta una vez, ya que nos crea el archivo
#archivo = open('texto.txt','a')
#archivo.write('Prueba de guardado wa')
#archivo.close()

#Ahora abrimos el archivo y solo vemos su contenido
#archivo =  open('texto.txt','r')
#print(archivo.read())


#Metodos internos
def encriptar(texto):
    print("El texto es: " + texto)
    textoFinal = '' 
    for letra in texto: 
        ascii = ord(letra)  #Cambiamos a los numeros Ascii
        ascii += 1     #Sumamos +1 a esos numeros
        textoFinal += chr(ascii)    #Esos numeros cambiados lo invertimos a letras

    return textoFinal

def desencriptar(texto):
    print("El texto es: " + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra) #Recuperamos el texto y cambiamos a Ascii
        ascii -= 1  #Esos numeros lo restamos para que nos de los numeros originales
        textoFinal += chr(ascii)    #Y lo cambiamos a letra :D
    return textoFinal 


#Metodos invocando al archivo y ponerlo a los metodos internos
def encriptarArchivo(linkFile):
    archivo = open(linkFile, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(linkFile, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print("Encriptado correctamente")


def desEncriptarArchivo(linkFile):
    archivo = open(linkFile, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(linkFile, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print("Desencriptado correctamente")


result = input("Presione E para encriptar, o D para desencriptar: ").upper()

linkFile = input("Ingrese la ruta del archivo: ")

if result == "E":
    encriptarArchivo(linkFile)
else:
    desEncriptarArchivo(linkFile)
