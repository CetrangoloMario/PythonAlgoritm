from Algoritmi_Ordinamento.bubble_sort import *
from Algoritmi_Ordinamento.naive_sort import *
from Algoritmi_Ordinamento.insert_sort import *
from Algoritmi_Ordinamento.merge_sort import *

list=[1,42,2134,2,2,31,243,12,3112]
size= len(list)
listaout=[]
#naiveSort(list,size)
#bubble_sort(list,size)
#insertSort(list,size)
mergeSort(list,0,size-1,listaout)


print(list)