"""
Autores:
Juan Andrés Romero Colmenares - 202013449
Luccas Rojas - 201923052
"""
import sys
def reservaEconomica(anio:int,a:float,b:float,c:float,d:float)->int:
    if(anio==0):
        return a
    elif(anio==1):
        return b
    else:
        ant=b
        antant=a
        i = 1
        while (i<anio):
            act=d*ant+c*antant
            antant=ant
            ant = act
            i+=1
        return act

def convolucionPonderada(anio:int,a:float,b:float,c:float,d:float)->int:
    res=0
    for i in range(anio+1):
        res += reservaEconomica(i,a,b,c,d)*reservaEconomica(anio-i,a,b,c,d)
    return round(res,4)

if __name__ == "__main__":
    contador = 0
    for caso in sys.stdin:
        linea = caso.strip("\n").strip().split(" ")
        if (len(linea)==5):
            try:
                print(convolucionPonderada(int(linea[0]),float(linea[1]),float(linea[2]),float(linea[3]),float(linea[4])))
            except KeyboardInterrupt:
                raise
            except Exception:
                print(0)