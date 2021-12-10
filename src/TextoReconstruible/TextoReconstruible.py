import sys
"""
Autores:
Juan Andrés Romero Colmenares - 202013449
Luccas Rojas - 201923052
"""
def textoReconstruible(lista:list[str])->str:
    aux = []
    aux2 = []
    auxi=""
    auxj=""
    auxStr=""
    cuenta = -1

    aux.extend(lista)

    while len(aux) != 1:
        for i in range(0, len(aux)):
            for j in range(i+1, len(aux)):
                numOverlap, strOverlap = overlap(aux[i], aux[j])
                if numOverlap>cuenta:
                    cuenta =numOverlap
                    auxStr = strOverlap
                    auxj= aux[j]
                    auxi= aux[i]
                elif numOverlap == cuenta and strOverlap not in aux2 and not isBlank(strOverlap):
                    aux2.append(strOverlap)

        if not isBlank(auxi):
            aux.remove(auxi)
        if not isBlank(auxj):
            aux.remove(auxj)
        if not isBlank(auxStr):
            aux.append(auxStr)

        if len(aux) == 0 and len(aux2) != 0:
            aux.extend(aux2)
            aux2 = []
            for string in lista:
                if not any(string in elemento for elemento in aux):
                    aux.append(string)
        elif len(aux2) == 0 and numOverlap == 0:
            res = ""
            for string in lista:
                res += string
            return res 
        auxStr=""
        auxi=""
        auxj=""
        cuenta = -1
    
    return aux[0]

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
            

def isBlank(cadena:str)->bool:
    if cadena == "" or cadena == " ":
        return True
    else:
        return False

def main():
    line = sys.stdin.readline().strip("\n").strip().split(" ")
    while (line is not None and len(line) > 0) and line[0] != "0":
        words = []
        listLength = int(line[0])
        line = sys.stdin.readline().strip("\n").strip().split(" ")
        for _ in range(listLength):
            words.append(line[0])
            line = sys.stdin.readline().strip("\n").strip().split(" ")
        print(textoReconstruible(words))
if __name__ == '__main__':
    main()
