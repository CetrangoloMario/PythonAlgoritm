
def trovaPoxMax(lista, dim):
    posMax=0
    for i in range(dim):
        if lista[posMax]<lista[i]:
            posMax=i
    #print("max: ",posMax)
    return posMax


def scambia(lista, pos1, pos2):
    #print("scambia")
    lista[pos1],lista[pos2]=lista[pos2],lista[pos1]

def insMinore(lista, pos):
    i=pos-1
    x=lista[pos]
    while i>=0 and x<lista[i]:
        lista[i+1]=lista[i]     #crea spazio
        i=i-1

    lista[i+1]=x
