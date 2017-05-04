import re #Se importa la librería necesaria para trabajar con expresiones regulares.
contador_lenguajes = 1 #Se inicializa el contador de lenguajes.
bandera_inicio = False #Se inicializa la bandera que dará inicio a la búsqueda de lenguajes.
patron_inicio = re.compile('[\*\s]{5,7}') #Se establece la expresion regular que indicará el inicio de la búsqueda de lenguajes. Se buscarán de 5 a 7 asteriscos y/o espacios.
patron_lenguaje = re.compile('^[\w\*][^":,]* -') #Se establece la expresión regular que filtrará los lenguajes.
#^[\w\*] => Se busca al inicio de la línea que el primer caracter sea alfanumérico o asterisco.
#[^":,]* - => Después se puede tener cualquier número de caracteres que no sean comillas dobles, dos puntos ni comas, y que después del último caracter haya un espacio y un guion.
patron_fin = re.compile('={7}') #Se establece la expresion regular que indicará el fin de la búsqueda de lenguajes. Se buscarán 7 signos de igualdad juntos.
with open("LANGUAGE.TXT", encoding="utf-8") as archivo: #Se abre el archivo y se guarda en la variable "archivo".
    for linea in archivo: #Se comienza un ciclo para recorrer línea por línea el contenido.
    	if not bandera_inicio: #Se verifica si la bandera de inicio es Falsa.
    		if patron_inicio.findall(linea): bandera_inicio = True #Si se encuentra el patron de inicio, se activa la bandera cambiando su valor a Verdadero.
    	else: #Si la bandera de inicio es Verdadera.
    		lenguaje = patron_lenguaje.findall(linea) #Se busca el patrón de lenguajes en cada línea y las coincidencias se almacenan en "lenguaje".
    		if lenguaje: #Si existe algo en "lenguaje".
    			print(contador_lenguajes, lenguaje[0].split(" -")[0]) #Se imprime en pantalla el contador de lenguajes y el nombre del lenguaje, separando por el " -" y mostrando solo la primer parte. Ej: "Java -" => "Java"
    			contador_lenguajes = contador_lenguajes + 1 #Se incrementa el contador de lenguajes.
    		if patron_fin.findall(linea): #Se verifica el patrón de termino.
    			break #Al encontrar coincidencia se termina el ciclo.
