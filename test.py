import hashlib

texto = "teste"

resultado = hashlib.md5(texto.encode()).hexdigest()

print(resultado)