"""
Haciendo uso de la función hash MD5 de la librería “cryptography”,
programa una función que calcule el hash MD5 de los ficheros “WinMD5.exe”
y “WinMD5_2.exe”. Tienes los ejecutables en el fichero adjunto. Es importante
que esta tarea se realice mediante programación e Python y utilizando la
librería Cryptography (no otra).

Fuente Hash:
https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/?highlight=hash#md5
"""

# Llamo la librería y las funciones que necesito para hacer el Hash
from cryptography.hazmat.primitives import hashes

# Aqui le indico a las funciones de la libreria que tipo de HASH quiero
# en mi caso MD5
digest = hashes.Hash(hashes.MD5())

# La función open() me permite abrir el archivo y con "rb" me permite decir
# que quiero leer el archivo en bytes que es lo que entiende los hashes
# luego cierro el archivo abierto
archivo = open("WinMD5.exe","rb")
leer = archivo.read()
archivo.close()

# A partir de aqui lo que hago es cargar el archivo convertirlo en MD5
# Luego finalizo la carga de HASH  MD5
# Imprimo en pantalla en modo Hexadecimal
digest.update(leer)
md5 = digest.finalize()
md5 = md5.hex()
print(md5)