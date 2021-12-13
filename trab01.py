# Natália Sens Weise

# matriz = [
#      [0, 0, 0, 1],
#      [1, 0, 0, 1],
#      [1, 0, 0, 1],
#      [0, 0, 1, 0]
#  ]

# matriz = [
# [0, 1, 1],    
# [1, 0, 1],    
# [1, 1, 0],    
  
# ]

# matriz = [
#     [0, 1, 1, 1],
#     [1, 1, 2, 1],
#     [1, 2, 0, 1],
#     [1, 1, 1, 0]
# ]

matriz=[
   [0, 2, 0],
   [2, 0, 0],
   [0, 0, 2]
]


def getGraus(matriz):
    listaGraus = []
    for linha in range(matriz.__len__()):
        l = 0
        for coluna in range(matriz.__len__()):
            l += matriz[linha][coluna]
        listaGraus.append(l)
    return listaGraus

def getGrauEntrada(matriz):
    listaGraus = []
    for coluna in range(matriz.__len__()):
        c = 0
        for linha in range(matriz.__len__()):
            c += matriz[linha][coluna]
        listaGraus.append(c)
    return listaGraus

def isDirigido(matriz):
    dirigido = False
    for linha in range(matriz.__len__()):
        for coluna in range(matriz.__len__()):
            if coluna == matriz.__len__()-1 and linha == matriz.__len__()-1:
                break
            if (matriz[linha][coluna]!=matriz[coluna][linha]):
               dirigido = True
    return dirigido

def isMultigrafo(matriz):
    multigrafo = False
    for linha in range(matriz.__len__()):
        for coluna in range(matriz.__len__()):
            if matriz[linha][coluna] > 1:
                multigrafo = True
            if linha == coluna:
                if matriz[linha][coluna] > 0:
                    multigrafo = True
    return multigrafo

def isCompleto(matriz):
    if (isMultigrafo(matriz)):
        return False
    else:
        for linha in range(matriz.__len__()):
            for coluna in range(matriz.__len__()):
                if coluna == linha:
                    if matriz[linha][coluna] != 0:
                        return False
                if coluna != linha:
                    if matriz[linha][coluna] != 1:
                        return False
        return True

def isRegular(matriz):
    listaGraus = getGraus(matriz)
    
    for i in range(listaGraus.__len__()):
        if i+1 < listaGraus.__len__()-1:
            if listaGraus[i] != listaGraus[i+1]:
                return False
        if listaGraus[i] != listaGraus[listaGraus.__len__()-1]:
            return False
    return True

def isNulo(matriz):
    for linha in range(matriz.__len__()):
        for coluna in range(matriz.__len__()):
            if matriz[linha][coluna] != 0:
                return False
    return True
    
def tipoDoGrafo(matriz):
    resultado="---------------------\n"
    resultado += "Grafo "
    if isDirigido(matriz):
        resultado+="Dirigido "
    else:
        resultado+="Não-dirigido "
    
    if isMultigrafo(matriz):
        resultado+="Multigrafo, "
    else:
        resultado+="Simples, "

    if isCompleto(matriz):
        resultado+="Completo, "
    else:
        resultado+="Não-completo, "

    if isRegular(matriz):
        resultado+="Regular e "
    else:
        resultado+="Não-regular e "
    
    if isNulo(matriz):
        resultado+="Nulo."
    else:
        resultado+="Não-nulo."

    return resultado

def grausDoVertice(matriz):
    listaGraus = getGraus(matriz)
    resposta = ""
    cont = 0
    dirigido = isDirigido(matriz)
    resposta+="---------------------\n"
    if dirigido:
        resposta+="Graus de Saída:\n"
    for i in listaGraus:
        resposta+="Vértice %i de grau %i \n" %(cont, i)
        cont+=1
    if dirigido:
        lista = listaGraus
    else:
        lista = sorted(listaGraus)
    resposta+="Sequência de graus: "
    for l in lista:
        resposta+=str(l)+" "

    if dirigido:
        cont = 0
        listaEntrada = getGrauEntrada(matriz)
        resposta+="\n---------------------\n"
        resposta+="Graus de Entrada:\n"
        for i in listaEntrada:
            resposta+="Vértice %i de grau %i \n" %(cont, i)
            cont+=1
        lista = listaEntrada
        resposta+="Sequência de graus: "
        for l in lista:
            resposta+=str(l)+" "
    return resposta

def arestasDoGrafo(matriz):
    qtdArestas = 0
    conjArestas="---------------------\n"
    conjArestas += "Conjunto de Arestas:\n"
    conjArestas+="{ "
    for linha in range(matriz.__len__()):
        for coluna in range(matriz.__len__()):
            if matriz[linha][coluna] != 0:           
                if linha == coluna:
                    c = 0
                    while c < matriz[linha][coluna]:
                        c +=1
                        conjArestas += "("+str(linha)+", "+str(coluna)+") "
                        conjArestas += "("+str(linha)+", "+str(coluna)+") "
                else:
                    conjArestas += "("+str(linha)+", "+str(coluna)+") "
                    if matriz[linha][coluna] > 1:
                        c = 1
                        while c < matriz[linha][coluna]:
                            c +=1
                            conjArestas += "("+str(linha)+", "+str(coluna)+") "

    conjArestas += "}\n"
    qtdArestas = contadorArestas(matriz)

    if not isDirigido(matriz):
        qtdArestas = int(qtdArestas/2)
        resposta = conjArestas+"Quantidade de Arestas: "+str(qtdArestas)
        resposta+="\n---------------------"
        return resposta
    else:
        resposta = conjArestas+"Quantidade de Arestas: "+str(qtdArestas)
        resposta+="\n---------------------"
        return resposta

def contadorArestas(matriz):
    arestas = 0
    for linha in range(matriz.__len__()):
        for coluna in range(matriz.__len__()):
            if not (isDirigido(matriz)):
                if linha==coluna:
                    arestas+=(matriz[linha][coluna]*2)
                else:
                    arestas+=matriz[linha][coluna]
            else:
                arestas+=matriz[linha][coluna]
    return arestas

print(tipoDoGrafo(matriz))
print(grausDoVertice(matriz))
print(arestasDoGrafo(matriz))