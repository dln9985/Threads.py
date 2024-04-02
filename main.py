from lib import *
import threading
import time

"""def Contador():
    print("Haciendo tiempo...")
    time.sleep(2) #segundos
    print("Tiempo hecho...")

t0 = time.time()

listaHilos = []

for i in range(4):
    t = threading.Thread(target=Contador)
    listaHilos.append( t )
    t.start()

for t in listaHilos:
    t.join()
    
tf = time.time() - t0

print(f"Tiempo total de ejecución: {tf}")
"""

print("")
print("Hilo Principal o 1 hilo")
def Enumerador( inicio, fin ):
    arrayNum = []
    for i in range ( inicio, fin+1 , 1):
        arrayNum.append(i)
        time.sleep(0.01)
    return arrayNum

t0 = time.time()
listaNumeros = Enumerador(1,100)
tf = time.time() - t0
print(f"Tiempo de ejecución: {tf}")
print (listaNumeros)
print("")
print("----------------------------------------")

print("")
print("Usando 2 hilos")

globalarrayNum = []
def EnumeradorDos( inicio, fin ):
    for i in range ( inicio, fin+1 , 1):
        globalarrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos= []
t= threading.Thread(target=EnumeradorDos, args=(1,50))
listaHilos.append(t)
t.start()
t= threading.Thread(target=EnumeradorDos, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()

tf = time.time() - t0

globalarrayNum.sort()
print(f"Tiempo de ejecución: {tf}")
print (globalarrayNum)

print("")
print("----------------------------------------")

print("")
print("Usando 4 hilos")

globarrayNum = []
def EnumeradorTres( inicio, fin ):
    for i in range ( inicio, fin+1 , 1):
        globarrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos= []
for i in range(4):
    t = threading.Thread(target=EnumeradorTres, args=(1,100))
    listaHilos.append(t)
    t.start()

for t in listaHilos:
    t.join()

tf = time.time() - t0

globarrayNum.sort()
print(f"Tiempo de ejecución: {tf}")
print (globarrayNum)
print("")

exit()