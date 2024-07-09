# YogiTypeCup es un torneo escrito puramente en Python que sirve para enfrentarse con tus amigos para ver quién es el que escribe mejor, siguiendo el principal parámetro: la rapidez en escribir.
# YogiTypeCup è un torneo scritto puramente in Python che serve per confrontarti ai tuoi amici per vedere chi è quello cue scrive meglio, seguendo il principale parametro: la velocitá nello scrivere.

import datetime, random, time



print("Primera Ronda")
#print("Prima Fase")
print("")
print("Consistirá en la escritura rápida")
#print("Consisterà nella scrittura veloce")

textos = ("Este juego te hará un maestro de escritura rápida.", "Nuestra mayor gloria no es no caer nunca, sino levantarnos cada vez que nos caemos.", "El futuro pertenece a aquellos que creen en la belleza de sus sueños.", "El optimismo puede ser más poderoso que un escuadrón de tanques.", "La vida es como montar en bicicleta. Para mantener el equilibrio tienes que avanzar.", "Las cosas terminan, pero los recuerdos durarán para siempre.", "Hacen falta días malos para darte cuenta de lo bonitos que son el resto.", "Es preciso soñar, pero con la condición de creer en nuestros sueños.", "Cuando salgas de esa tormenta, no serás la misma persona que entró en ella.", "El amor no necesita ser entendido, simplemente necesita ser demostrado.", "Tardé un minuto en conocerte, pero me tomará toda una vida llegar a olvidarte.", "Amar no es nada, ser amado es algo. Amar y ser amado lo es todo.", "La vida es como una gran tormenta: puede asustarnos, pero también puede limpiar el camino para algo nuevo.", "Hay tres cosas en la vida que nunca debes perder: tu sonrisa, tu alegría y tu forma de ser.", "La felicidad en la vida consiste en tener siempre algo que hacer, alguien a quien amar y algo que esperar.", "Aprende del pasado, si quieres que el presente sea mejor que el pasado. Considera que ocurrió en el pásado. Aprende algo valioso de ello. Actúa distinto en el presente.", "Receta para una vida feliz: una pizca de sonrisas, una buena compañía y muchas ganas de vivirla.", "Los años que tienes son aquellos que ya no tienes. Solo tienes los años que te quedan por vivir.", "El sueño de todos puede hacerse realidad si te limitas a él y trabajas duro.", "Lo que separa al individuo talentoso del exitoso es un montón de trabajo duro.", "En toda historia de éxito encontrarás a alguien que tomó una decisión valiente.")

textos1 = list(textos)

class Jugador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.prueba1 = datetime.timedelta(0, 0, 0)
		self.prueba2 = datetime.timedelta(0, 0, 0)
		self.prueba3 = datetime.timedelta(0, 0, 0)
		self.tiempofinal = datetime.timedelta(0, 0, 0)

	def primeraupdate(self, valor1):
		self.prueba1 = valor1
	def segundaupdate(self, valor1):
		self.prueba2 = valor1
	def terceraupdate(self, valor1):
		self.prueba3 = valor1
	def sumatiempo(self):
		self.tiempofinal = self.prueba1 + self.prueba2 + self.prueba3

request = "The091011"
requestintmas = 91011
while requestintmas < 2 or requestintmas > 8:
	requestintmas = int(input("Cuántos jugadores van a jugar (min. 2, máx. 8)?: "))
requestint = requestintmas
if requestint == 8:
	request = input("Cuál es su nombre?: ")
	jug8 = Jugador(request)
	requestint -= 1
if requestint == 7:
	request = input("Cuál es su nombre?: ")
	jug7 = Jugador(request)
	requestint -= 1
if requestint == 6:
	request = input("Cuál es su nombre?: ")
	jug6 = Jugador(request)
	requestint -= 1
if requestint == 5:
	request = input("Cuál es su nombre?: ")
	jug5 = Jugador(request)
	requestint -= 1
if requestint == 4:
	request = input("Cuál es su nombre?: ")
	jug4 = Jugador(request)
	requestint -= 1
if requestint == 3:
	request = input("Cuál es su nombre?: ")
	jug3 = Jugador(request)
	requestint -= 1
if requestint == 2:
	request = input("Cuál es su nombre?: ")
	jug2 = Jugador(request)
	requestint -= 1
if requestint == 1:
	request = input("Cuál es su nombre?: ")
	jug1 = Jugador(request)
	requestint -= 1

frase1 = random.choice(textos1)
textos1.remove(frase1)
frase2 = random.choice(textos1)
textos1.remove(frase2)
frase3 = random.choice(textos1)
textos1.remove(frase3)


class Jueguitos:
	def __init__(self, jug, frase1, frase2, frase3):
		self.jugador = jug
		self.frase1 = frase1
		self.frase2 = frase2
		self.frase3 = frase3

	def juegofrase1(self, frase1):
		print(f"Estás listo/a {self.jugador.nombre}?")
		time.sleep(1)
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("GO!")
		print(frase1)
		frasef = "-"
		valor1 = datetime.datetime.now()
		while frase1 != frasef:
			frasef = input("")
		valor2 = datetime.datetime.now()
		print("Exacto!")
		valorf = valor2 - valor1
		self.jugador.primeraupdate(valorf)
		self.jugador.sumatiempo()
	def juegofrase2(self, frase2):
		print(f"Estás listo/a {self.jugador.nombre}?")
		time.sleep(1)
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("GO!")
		print(frase2)
		frasef = "-"
		valor1 = datetime.datetime.now()
		while frase2 != frasef:
			frasef = input("")
		valor2 = datetime.datetime.now()
		print("Exacto!")
		valorf = valor2 - valor1
		self.jugador.segundaupdate(valorf)
		self.jugador.sumatiempo()
	def juegofrase3(self, frase3):
		print(f"Estás listo/a {self.jugador.nombre}?")
		time.sleep(1)
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("GO!")
		print(frase3)
		frasef = "-"
		valor1 = datetime.datetime.now()
		while frase3 != frasef:
			frasef = input("")
		valor2 = datetime.datetime.now()
		print("Exacto!")
		valorf = valor2 - valor1
		self.jugador.terceraupdate(valorf)
		self.jugador.sumatiempo()

# anothing = input("Press Enter:")

def tabladetiempos(listadetiempos):
	listadetiempos.sort(key=lambda x: x.tiempofinal, reverse=False)
	print("Tabla de tiempos:")
	lenghtmax = len(listadetiempos)
	lenghtmin = 1
	for tiempo in listadetiempos:
		print(f"{lenghtmin}. {tiempo.nombre} | {tiempo.tiempofinal}")
		lenghtmin += 1
	return ""

a = Jueguitos(jug1, frase1, frase2, frase3)
b = Jueguitos(jug2, frase1, frase2, frase3)
try:
	c = Jueguitos(jug3, frase1, frase2, frase3)
except NameError:
	print("")
try:
	d = Jueguitos(jug4, frase1, frase2, frase3)
except NameError:
	print("")
try:
	e = Jueguitos(jug5, frase1, frase2, frase3)
except NameError:
	print("")
try:
	f = Jueguitos(jug6, frase1, frase2, frase3)
except NameError:
	print("")
try:
	g = Jueguitos(jug7, frase1, frase2, frase3)
except NameError:
	print("")
try:
	h = Jueguitos(jug8, frase1, frase2, frase3)
except NameError:
	print("")

a.juegofrase1(frase1)
b.juegofrase1(frase1)
try:
	c.juegofrase1(frase1)
except NameError:
	print("")
try:
	d.juegofrase1(frase1)
except NameError:
	print("")
try:
	e.juegofrase1(frase1)
except NameError:
	print("")
try:
	f.juegofrase1(frase1)
except NameError:
	print("")
try:
	g.juegofrase1(frase1)
except NameError:
	print("")
try:
	h.juegofrase1(frase1)
except NameError:
	print("")

listadetiempos =  [jug1, jug2]
try:
	listadetiempos.append(jug3)
except NameError:
	print("")
try:
	listadetiempos.append(jug4)
except NameError:
	print("")
try:
	listadetiempos.append(jug5)
except NameError:
	print("")
try:
	listadetiempos.append(jug6)
except NameError:
	print("")
try:
	listadetiempos.append(jug7)
except NameError:
	print("")
try:
	listadetiempos.append(jug8)
except NameError:
	print("")

listadetiemposmas = listadetiempos
print(tabladetiempos(listadetiemposmas))

a.juegofrase2(frase2)
b.juegofrase2(frase2)
try:
	c.juegofrase2(frase2)
except NameError:
	print("")
try:
	d.juegofrase2(frase2)
except NameError:
	print("")
try:
	e.juegofrase2(frase2)
except NameError:
	print("")
try:
	f.juegofrase2(frase2)
except NameError:
	print("")
try:
	g.juegofrase2(frase2)
except NameError:
	print("")
try:
	h.juegofrase2(frase2)
except NameError:
	print("")

listadetiempos =  [jug1, jug2]
try:
	listadetiempos.append(jug3)
except NameError:
	print("")
try:
	listadetiempos.append(jug4)
except NameError:
	print("")
try:
	listadetiempos.append(jug5)
except NameError:
	print("")
try:
	listadetiempos.append(jug6)
except NameError:
	print("")
try:
	listadetiempos.append(jug7)
except NameError:
	print("")
try:
	listadetiempos.append(jug8)
except NameError:
	print("")
listadetiemposmas = listadetiempos
print(tabladetiempos(listadetiemposmas))

a.juegofrase3(frase3)
b.juegofrase3(frase3)
try:
	c.juegofrase3(frase3)
except NameError:
	print("")
try:
	d.juegofrase3(frase3)
except NameError:
	print("")
try:
	e.juegofrase3(frase3)
except NameError:
	print("")
try:
	f.juegofrase3(frase3)
except NameError:
	print("")
try:
	g.juegofrase3(frase3)
except NameError:
	print("")
try:
	h.juegofrase3(frase3)
except NameError:
	print("")

listadetiempos =  [jug1, jug2]
try:
	listadetiempos.append(jug3)
except NameError:
	print("")
try:
	listadetiempos.append(jug4)
except NameError:
	print("")
try:
	listadetiempos.append(jug5)
except NameError:
	print("")
try:
	listadetiempos.append(jug6)
except NameError:
	print("")
try:
	listadetiempos.append(jug7)
except NameError:
	print("")
try:
	listadetiempos.append(jug8)
except NameError:
	print("")

listadetiemposmas = listadetiempos
print(tabladetiempos(listadetiemposmas))
time.sleep(7.5)