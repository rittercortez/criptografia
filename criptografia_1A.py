"""
a)	El ejercicio consiste en cifrar el mensaje “a secret message”
con la clave '12345678901234567890123456789012'.

Utiliza el modo de cifrado CBC. Descifra el criptograma y comprueba
que obtienes el texto original. Explica cómo has desarrollado el ejercicio
y aporta capturas de pantalla que apoyen tu explicación. Además, aporta el
fichero .py que has generado.

#Fuente cifrado:
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption
/?highlight=cifrado%20en%20aes#cryptography.hazmat.primitives.ciphers.algorithms.AES

#Fuente Modo Cifrado CBC:
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/?highlight=cifrado%
20en%20aes#symmetric-encryption-modes

# Fuente default_backend():
https://cryptography.io/en/latest/hazmat/backends/?highlight=defalult_backend#cryptography.hazmat
.backends.default_backend

"""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# la clave por obligación tenemos que convertirla a bytes porque si la introducimos
# como numeros como caracteres str  no funcionara el encriptado
clave = (b'12345678901234567890123456789012')
# Para el modo CBC necesitamos una variable de inicializacion
vector_inicializacio =  os.urandom(16)

# Aqui escogemos el tipo de cifrado que queremos utilizar para la clave
# y su modo de cifrado en bloque que en nuestro caso es CBC
# "default_backend" nos permite recoger multiples backends criptográficos

modo_cifrado = Cipher(algorithms.AES(clave),modes.CBC(vector_inicializacio), backend=default_backend())
clave_cifrada = modo_cifrado.encryptor()


# Ciframos el texto claro utilizando la clave de cifrado
texto_claro = clave_cifrada.update(b"a secret message") + clave_cifrada.finalize()
# A partir de aqui podremos visualizar el texto en claro nuevamente
decifrar_conClave =  modo_cifrado.decryptor()
decifrado = decifrar_conClave.update(texto_claro) + decifrar_conClave.finalize()
print(texto_claro.hex())
print(decifrado)
