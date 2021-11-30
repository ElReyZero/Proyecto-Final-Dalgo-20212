def res(a,b):
    c=a-b
    if(c<0):
        return c*-1
    else:
        return c

def abs(i:int)->int:
    if (i<0):
        return i*-1
    else:
        return i


def grafBc(i:int,b:int,w:int,c:list)->int:
    b=0
    w=0
    if (i==0):
        w+=c[i][0]
        b+=c[i][1]
        return res(b,w)
    else:
        return min(grafBc(i-1,b+c[i][0],w+c[i][1],c),grafBc(i-1,b+c[i][1],w+c[i][0],c))
#print(grafBc(4,0,0,[[1,2],[1,2],[1,2],[1,2],[1,5]]))
def grafBc(i:int,sum:int,c:list)->int:
    #sum=0
    if (i==0):
        #sum-=c[i][0]
        #sum+=c[i][1]
        return abs(sum)
    else:
        return min(grafBc(i-1,sum-c[i][0]+c[i][1],c),grafBc(i-1,sum+c[i][0]-c[i][1],c))
#print(grafBc(4,0,[[1,2],[1,2],[1,2],[1,2],[1,5]]))
#print(grafBc(1,0,[[1,2],[3,2]]))
"""
def subconjuntoMinimo(i:int,lista:list,suma:int)->int:
    if (i==0):
        return suma+lista[i]
    else:
        sum=subconjuntoMinimo(i-1,lista,abs(suma-lista[i]))
        res=subconjuntoMinimo(i-1,lista,abs(suma+lista[i]))
        return min(sum,res)
print("el min suma es:",subconjuntoMinimo(4,[0,1,1,1,3],0))
print("el min suma es:",subconjuntoMinimo(2,[0,2,1],0))
print("el min suma es:",subconjuntoMinimo(2,[0,0,1],0))
print("el min suma es:",subconjuntoMinimo(3,[0,0,1,1],0))
print("el min suma es:",subconjuntoMinimo(5,[0,1,8,20,2,3],0))
print("el min suma es:",subconjuntoMinimo(4,[1,8,20,2,3],0))
"""
def subconjuntoMinimo(i:int,lista:list,suma:int)->int:
    if (i==0):
        return suma
    else:
        sum=subconjuntoMinimo(i-1,lista,abs(suma-lista[i]))
        res=subconjuntoMinimo(i-1,lista,abs(suma+lista[i]))
        return min(sum,res)
print("el min suma es:",subconjuntoMinimo(3,[1,1,1,3],0))
print("el min suma es:",subconjuntoMinimo(1,[2,1],0))
print("el min suma es:",subconjuntoMinimo(2,[0,0,1],0))
print("el min suma es:",subconjuntoMinimo(3,[0,0,1,1],0))
print("el min suma es:",subconjuntoMinimo(5,[0,1,8,20,2,3],0))
print("el min suma es:",subconjuntoMinimo(4,[1,8,20,2,3],0))
