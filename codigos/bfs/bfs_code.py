def findLevel(vertices,arestas, verticeAlvo):
    maxVertex=0
    for index in arestas:
        maxVertex=max(maxVertex,max(index[0],index[1]))
    
    adjacente=[[] for j in range(maxVertex+1)]
    
    for i in range(len(arestas)):
        adjacente[arestas[i][0]].append(arestas[i][1])
        adjacente[arestas[i][1]].append(arestas[i][0])
    
    
    if(verticeAlvo>maxVertex or len(adjacente[verticeAlvo])==0):
        return -1
    
    fila=[]
    fila.append(0)
    level=0
    
    visitado=[0]*(maxVertex+1)
    visitado[0]=1
    
    while(len(fila)>0):
        tamanhoFila=len(fila)
        while(tamanhoFila>0):
            verticeAtual=fila[0]
            fila.pop(0)
            if(verticeAtual==verticeAlvo):
                return level
            for index in adjacente[verticeAtual]:
                #print(adjacente[verticeAtual])
                if(not visitado[index]):
                    fila.append(index)
                    visitado[index]=1
            tamanhoFila=tamanhoFila-1
        level=level+1
        
    return -1

vertices=5
arestas=[[0,1],[0,2],[1,3],[2,4]]
alvo=3

level=findLevel(vertices,arestas,alvo)
print(level)