def abs(i:int)->int:
    if (i<0):
        return i*-1
    else:
        return i

def subconjuntoMinimoFirst(i:int,lista:list,suma:int)->int:
    if (i==0):
        return suma
    else:
        sum=subconjuntoMinimoFirst(i-1,lista,abs(suma-lista[i]))
        res=subconjuntoMinimoFirst(i-1,lista,abs(suma+lista[i]))
        return min(sum,res)

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
arr6 = [1,11,6,5]
arr7 = [36,7,46,40]
arr7a = [0,36,7,46,40]
print("el min suma es:",subconjuntoMinimo(len(arr1)-1,arr1,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr2)-1,arr2,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr3)-1,arr3,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr4)-1,arr4,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr5)-1,arr5,0, 0))
print("el min suma es:",subconjuntoMinimo(len(arr7)-1,arr7,0, 0))
print("el min suma 2 es:",subconjuntoMinimoFirst(len(arr7a)-1,arr7a,0))

def subconjuntoMinimoPD(lista:list)->int:
    #Suma de los elementos de la lista
    total_sum = sum(lista)
    n = len(lista)
    #Matriz de len(lista) * la mitad de la suma de los números en el arreglo
    matriz = [[False for j in range((total_sum//2)+1)] for i in range(n+1)]
    # Se llena la primera fila con True
    for i in range(len(matriz)):
      matriz[i][0] = True
    for i in range(1, len(matriz)):
      for j in range(1,len(matriz[0])):
          if lista[i-1] <= j:
            matriz[i][j] = matriz[i-1][j-lista[i-1]] or matriz[i-1][j]
          else:
             matriz[i][j] = matriz[i-1][j]
            
    minimo = float('inf')
    for i in range(len(matriz[0])-1, -1, -1):
      if matriz[-1][i]:
         minimo = min(minimo, abs(total_sum-(2*i)))
         return minimo
        
print(subconjuntoMinimoPD([0,1]))