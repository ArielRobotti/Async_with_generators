import time

#-------- Cuenta regresiva asincronica basada en generadores ----------------
def asyncCount(start, _t):
	if start//1 != start or start <= 0 or _t <= 0: #Validacion de parametros de entrada
		raise ValueError ("Solo numeros mayores que 0 y enteros positivos para start")
	for i in range(start, 0, -1):
		print(i)                     #Efectúa la tarea principal que en este caso es imprimir el valor actual del contador
		t0 = time.time()             #Se fija un tiempo de referencia t0
		while time.time() < t0 + _t: 
			yield                    #Cederá constantemente el control de ejecución mientras no haya transcurrido el tiempo _t desde t0
	print(0)

#------------- Creamos dos generadores mediante la funcion definida anteriormente, con diferentes valores ---------
count_d1 = asyncCount(10,2)
count_d2 = asyncCount(50,0.125)

tareas = [count_d1,count_d2]        #Los incluimos en una lista de tareas

while tareas != []:                 #Mientras la lista de tareas tenga alguna tarea pendiente
	current = tareas.pop()          #se extraerá la ultima de ellas para
	try:                            #intentar ejecutarla hasta su
		next(current)               #siguiente yield en caso de que lo tuviera, caso contrario se capturara la excepcion
		tareas = [current] + tareas #Luego se volvera a colocar la tarea al inicio de la lista
	except StopIteration:           #En caso de que la tarea ya no tenga ningun yield pendiente, 
		pass                        #simplemente no se la vuelve a incluir en la lista de tareas

