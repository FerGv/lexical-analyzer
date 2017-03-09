import re #Se importa la librería necesaria para trabajar con expresiones regulares.
contador_lenguajes = 1 #Se inicializa el contador de lenguajes.
bandera_inicio = False #Se inicializa la bandera que dará inicio a la búsqueda de lenguajes.
archivo = open("LANGUAGE.TXT") #Se abre el archivo y se guarda en la variable "archivo".
contenido = archivo.readlines() #Se leen todas la líneas del archivo y se guardan en la variable "contenido".
patron_inicio = re.compile('[\*\s]{5,7}') #Se establece la expresion regular que indicará el inicio de la búsqueda.
patron_lenguaje = re.compile('^[\w\*][^":,]* -') #Se establece la expresion regular que filtrará los lenguajes.
patron_fin = re.compile('={7}') #Se establece la expresion regular que indicará el fin de la búsqueda.
for linea in contenido: #Se comienza un ciclo para recorrer línea por línea el contenido.
	if not bandera_inicio: #Se verifica si la bandera de inicio es Falsa.
		if patron_inicio.findall(linea): bandera_inicio = True #Si se encuentra el patron de inicio, se activa la bandera cambiando su valor a Verdadero.
	else: #Si la bandera de inicio es Verdadera.
		lenguaje = patron_lenguaje.findall(linea) #Se busca el patrón de lenguajes en cada línea y las coincidencias se almacenan en "lenguaje".
		if lenguaje: #Si existe algo en "lenguaje".
			print(contador_lenguajes, lenguaje[0].split(" -")[0]) #Se imprime en pantalla el contador de lenguajes y el nombre del lenguaje, separando por el " -" y mostrando solo la primer parte. Ej: "Java -" => "Java"
			contador_lenguajes = contador_lenguajes + 1 #Se incrementa el contador de lenguajes.
		if patron_fin.findall(linea): #Se verifica el patrón de termino.
			break #Al encontrar coincidencia se termina el ciclo.
