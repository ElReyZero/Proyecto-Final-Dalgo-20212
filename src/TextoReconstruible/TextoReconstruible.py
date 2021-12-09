import time
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
    start_time = time.time()
    #print(textoReconstruible(["RRRRRRRRRRRR", "RRRRRRRRRRRR", "RRRRRRRRRRRR", "RRRRRRRRRRRR", "RRRRRRRRRRRR", "RRRRRRRRRRRR"]))
    #print(textoReconstruible(["nfid", "conf", "cial", "denc", "onfi", "enci"]))
    #print(textoReconstruible(["aab","baa","aaa","bbb"]))
    #print(textoReconstruible(["abb","bbc","bbb"]))
    #print(textoReconstruible(["alex","loves","leetcode"]))
    #print(textoReconstruible(["catg","ctaagt","gcta","ttca","atgcatc"]))
    print(textoReconstruible(["efde","defab", "abcdef"]))
    print("%s segundos" % (time.time()-start_time))
if __name__ == '__main__':
    main()
