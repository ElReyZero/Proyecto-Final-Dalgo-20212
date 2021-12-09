

def overlap(a:str,b:str)-> tuple:
    max = 0
    len1 = len(a)
    len2 = len(b)
    strRes = ""
    for i in range(1, 1 + min(len(a), len(b))):
        if a[len1-i:] == b[0:i]:
            if max < i:
                max =i
                strRes = a + b[i:]

    for i in range(1, 1 + min(len(a), len(b))):
        if b[len2-i:len2] == a[0:i]:
            if max < i:
                max =i
                strRes = b + a[i:]
    return max, strRes


def textoReconstruible(lista:list[str], k:int)->str:
    aux = []
    auxi=""
    auxj=""
    auxStr=""
    for i in range(len(lista)):
        aux.append(lista[i])
    cuenta = -1
    while len(aux) != 1:
        for i in range(0, len(aux)):
            for j in range(i+1, len(aux)):
                numOverlap, strOverlap = overlap(aux[i], aux[j])
                if numOverlap>cuenta:
                    cuenta =numOverlap
                    auxStr = strOverlap
                    auxj= aux[j]
                    auxi= aux[i]
        
        if not isBlank(auxi):
            aux.remove(auxi)
        if not isBlank(auxj):
            aux.remove(auxj)
        if not isBlank(auxStr):
            aux.append(auxStr)
        auxStr=""
        auxi=""
        auxj=""
        cuenta = -1
    
    return aux[0]
            

def isBlank(cadena:str)->bool:
    if cadena == "" or cadena == " ":
        return True
    else:
        return False


def main():
    print(textoReconstruible(["aab","baa","aaa","bbb"], 3))

if __name__ == '__main__':
    main()