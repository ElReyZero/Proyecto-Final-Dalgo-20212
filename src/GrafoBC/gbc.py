def abs(i:int)->int:
    if (i<0):
        return i*-1
    else:
        return i
"""
def subconjuntoMinimo(i:int,lista:list,suma:int)->int:
    if (i==0):
        return suma
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
def subconjuntoMinimo(i:int,lista:list,total1:int, total2:int)->int:
    if i<0:
        return abs(total1 - total2)
    else:
        sum=subconjuntoMinimo(i-1,lista,total1, total2+lista[i])
        res=subconjuntoMinimo(i-1,lista,total1+lista[i], total2)
        return min(sum,res)

arr1 = [20,18,12,5,4,1,10,11,9,4,3,3]
arr2 = [2,1]
arr3 = [1,8,20,2,3]
arr4 = [0,1]
arr5 = [0,1,1]
print("el min suma es:",subconjuntoMinimo(len(arr1)-1,arr1,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr2)-1,arr2,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr3)-1,arr3,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr4)-1,arr4,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr5)-1,arr5,0, 0))