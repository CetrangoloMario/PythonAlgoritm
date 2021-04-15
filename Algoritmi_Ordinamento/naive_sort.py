
def trovaPoxMax(lista, dim):
    i,posMax=0,0
    for i in range(dim):
        if lista[posMax]<lista[i]:
            posMax=i
    print("max: ",posMax)
    return posMax


def scambia(lista, p, param):
    print("scambia")
    lista[p],lista[param]=lista[param],lista[p]




def naiveSort (lista, dim):
    p=0;
    while dim>1:
        p=trovaPoxMax(lista,dim)
        if p<(dim-1):
            scambia(lista,p,dim-1)

        dim=dim-1
    print(lista)


list=[1,42,2134,2,31,243,12,3112]
size= len(list)

print(list)

naiveSort(list,size)
