from utility import *

def naiveSort (lista, dim):
    p=0;
    while dim>1:
        p=trovaPoxMax(lista,dim)
        if p<(dim-1):
            scambia(lista,p,dim-1)

        dim=dim-1







