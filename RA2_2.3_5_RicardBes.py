# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/10/2024
# Versió: 1
#
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​
# Especificacions Programa que generi un nombre enter i imprimeix tots els nombres primers


# Funció per comprovar si un nombre és primer
def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Demanar un nombre enter a l'usuari
num = int(input("Introdueix un nombre enter: "))

# Imprimir tots els nombres primers des de 2 fins al nombre
print(f"\nNombres primers de 2 fins a {num}:\n")
for i in range(2, num + 1):
    if es_primer(i):
        print(i)