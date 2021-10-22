"""
En este apartado vamos a ver la diferencia entre los diferentes
modos de cifrado. Para ello se va a repetir el ejercicio anterior,
utilizando los modos de cifrado OFB, CFB, ECB.
Compara el criptograma obtenido en cada uno de los casos.

"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


clave = (b'12345678901234567890123456789012')

# NO requiere vector de inicialización
# Siempre se obtiene el mismo resultado
# Asi que un ataque de diccionario lo romperia con facilidad

modo_cifrado = Cipher(algorithms.AES(clave),modes.ECB(), backend=default_backend())
clave_cifrada = modo_cifrado.encryptor()

texto_claro = clave_cifrada.update(b"a secret message") + clave_cifrada.finalize()

decifrar_conClave =  modo_cifrado.decryptor()
decifrado = decifrar_conClave.update(texto_claro) + decifrar_conClave.finalize()
print(texto_claro.hex())
print(decifrado)