# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/10/2024
# Versió: 1
#
# Descripció: Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.
# Especificacions Programa que generi un nombre enter i calculi la suma de tots els nombres

num = int(input("Introdueix un nombre enter: "))

suma = 0
for i in range(1, num + 1):
    suma += i

print(f"La suma dels nombres de 1 fins a {num} és: {suma}")