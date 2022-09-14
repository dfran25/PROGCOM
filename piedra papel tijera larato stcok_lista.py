
import random

 
# Tipo enumerado de los posibles valores asociados a un codigo
(PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK) = range(5)
 
# Valores ordenados por posicion
valores = ["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"]
 
# Reglas del juego. La clave representa la posicion en el vector de valores. El valor de cada clave es la manera en que un elemento vence a otro y los elentos a los que puede vencer.
# Por ejemplo, la posicion 0 representa PIEDRA. PIEDRA aplasta a LAGARTO y PIEDRA aplasta a TIJERA
reglas = {0: [["aplasta", "aplasta"],[LAGARTO, TIJERA]], 1: [["tapa", "desautoriza"],[PIEDRA, SPOCK]], 2: [["corta", "decapita"],[PAPEL, LAGARTO]], 3: [["envenena", "come"],[SPOCK, PAPEL]], 4: [["rompe", "vaporiza"],[TIJERA, PIEDRA]]}
(GANAUSUARIO, GANAMAQUINA, EMPATE) = range(3)
 
# Obtiene una cadena de texto a partir del codigo de la tirada
# Ej: valorTexto(0) = PIEDRA
def valorTexto(codigo):
        return valores[codigo]
 
# Devuelve el codigo de la tirada a partir de la cadena de texto de la tirada
# Ej: textoValor("PIEDRA") = 0
def textoValor(texto):
        for i, valor in enumerate(valores):
                if (texto == valor):
                        return i
 
# Tirada de la maquina
def sacaMaquina():
        tirada = random.randint(0,5)
        return tirada;
 
# Tirada del usuario
def sacaUsuario():
        tirada = ""
        while not tirada in valores:
                tirada = input("Introduce una jugada valida (PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK): ")
        return textoValor(tirada);
 
# Valida la jugada
def juego(usuario, maquina):
        if maquina in reglas[usuario][1]:
                return GANAUSUARIO
        elif usuario in reglas[maquina][1]:
                return GANAMAQUINA
        else:
                return EMPATE
 
# Explica la jugada
# Ej: explica(TIJERA, PAPEL) =
def explica(ganador, perdedor):
        for i, valor in enumerate(reglas[ganador][1]):
                if (perdedor == valor):
                        print( valorTexto(ganador), reglas[ganador][0][i], valorTexto(perdedor))
 # CUERPO PRINCIPAL 

 
# Tiradas de los usuarios
usuario = sacaUsuario()
maquina = sacaMaquina()
print (valorTexto(usuario), "VS", valorTexto(maquina))
 
# Comprueba la jugada y muestra el resultado
resultado = juego(usuario, maquina)
if resultado == GANAUSUARIO:
        explica(usuario, maquina)
        print ("Has ganado!")
elif resultado == GANAMAQUINA:
        explica(maquina, usuario)
        print ("Has perdido!")
else:
        print ("Empate!")
