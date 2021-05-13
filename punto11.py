import numpy as np
import random
from A_estrella import A_star,nodos,nodo_inicial
#Dado un punto en el espacio articular de un robot serie de 6 grados de libertad, 
# encontrar el camino más corto para llegar hasta otro punto utilizando el algoritmo A*. 
# Genere aleatoriamente los puntos de inicio y fin, 
# y genere también aleatoriamente obstáculos que el robot debe esquivar, siempre en el espacio articular. 


n=12    # El paso es de 60°. Para esta discretizacion la complejidad puede ser de b^n = 1.5e17 (b=729 y n=6)
m=6     # Cantidad de obstaculos
d=6     # Dimension espacial
#R.qlim(1,1:2) = [-180,  180]*pi/180;
#R.qlim(2,1:2) = [-100,  100]*pi/180;
#R.qlim(3,1:2) = [-220,  60]*pi/180;
#R.qlim(4,1:2) = [-200, 200]*pi/180;
#R.qlim(5,1:2) = [-200, 200]*pi/180;
#R.qlim(6,1:2) = [-400, 400]*pi/180;
    
punto_inicial=[]
punto_inicial.append(random.randrange(-180,  180,n))
punto_inicial.append(random.randrange(-100,  100,n))
punto_inicial.append(random.randrange(-220,  60,n))
punto_inicial.append(random.randrange(-200, 200,n))
punto_inicial.append(random.randrange(-200, 200,n))
punto_inicial.append(random.randrange(-400, 400,n))

punto_final= []
punto_final.append(random.randrange(-180,  180,n))
punto_final.append(random.randrange(-100,  100,n))
punto_final.append(random.randrange(-220,  60,n))
punto_final.append(random.randrange(-200, 200,n))
punto_final.append(random.randrange(-200, 200,n))
punto_final.append(random.randrange(-400, 400,n))

obstaculos=[]
for i in range(m):
    obstaculos.append([random.randrange(0,360, n) for i in range(d)])


camino_A=[]
camino_B=[]
posicion=A_star(punto_inicial[0:3],punto_final[0:3],3,12,obstaculos)
posicion_int=posicion.buscar_camino()

for i in range(len(posicion_int)-1):
    posicion=A_star(posicion_int[i+1],posicion_int[i],3,1,obstaculos)
    camino_A.extend(posicion.buscar_camino())

orientacion=A_star(punto_inicial[3:6],punto_final[3:6],3,12,obstaculos)
posicion_int=orientacion.buscar_camino()
for i in range(len(posicion_int)-1):
    orientacion=A_star(posicion_int[i+1],posicion_int[i],3,1,obstaculos)
    camino_B.extend(orientacion.buscar_camino())

print(f"El mejor camino entre [{punto_inicial}, {punto_final}] es:\n")
print("qt = [")

while len(camino_A)>len(camino_B):
    camino_B.append(camino_B[-1])

while len(camino_B)>len(camino_A):
    camino_A.append(camino_A[-1])

for q in zip(camino_A,camino_B):
    print(f"       {q}".replace(","," ").replace("(","").replace(")","").replace("[","").replace("]",""),"")

print("];")
