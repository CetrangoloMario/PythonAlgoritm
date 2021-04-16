from utility import *

def bubble_sort (lista, dim):
    ordinato=0
    while dim>1 and ordinato==0:
        ordinato=1

        for i in range(dim-1):
            if lista[i]> lista[i+1]:
                scambia(lista,i,i+1)
                ordinato=0
        dim=dim-1

