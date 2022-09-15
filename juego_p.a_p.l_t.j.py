# Ejercicio de juego 1: realizar un juego de piedra-papel o tijera


print("----------------------------------")
print("----juego-piedra-papel-tiejera----")
print("----------------------------------")

import random 
while True:
   
    aleatorio = random.randrange (0,3 )
    elije = ""
print("___1. piedra____")
print("___2. papel_____")
print("___3. tijera____")
opcion = int(input)("ELIGE LA OPCION QUE QUIERA:")

if opcion == 1:
    elijeusuario = "piedra"
elif opcion == 2:
    elijeusuario = "papel"
elif opcion == 3:
    elijeusuario = "tijera"
print("Elegite:", elijeusuario)

if aleatorio == 0:
    elige = "piedra"
elif aleatorio == 1:
    elige = "papel"
elif aleatorio == 2:
    elige = "tijera"
print("la maquina eligio: ", elige )
print("...")
if elije == " piedra " and eligeusuario == "papel":
    print("Ganaste, papel envuelve piedra")


elif elije == " papel " and eligeusuario == "tijera":
    print("Ganaste, tijera  corta papel")

elif elije == " tijera " and eligeusuario == "tijera":
    print("perdiste, piedra machaca tijera")


if elije == " papel " and eligeusuario == "piedra":
    print("perdiste, papel envuelve piedra")

elif elije == " tijera " and eligeusuario == "papel":
    print("perdiste, tijera  corta papel")

elif elije == " piedra " and eligeusuario == "tijera":
    print("perdiste, piedra machaca tijera")

elif elije == eligeusuario:
    print("empate")



