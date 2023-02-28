def imprimir_arreglo(arreglo):
  for i in range(len(arreglo)-1):
    print(f"[{arreglo[i]}]",end="")
def algoritmo_burbuja(arreglo):
  for i in range(len(arreglo)-1):
    for j in range(len(arreglo)-1-i):
      if arreglo[j]> arreglo[j+1]:
        aux=arreglo[j]
        arreglo[j]=arreglo[j+1]
        arreglo[j+1]=aux

        
listaSueldos=[20.8,150.5,170.5,180.8,190,30,75.6,200]
imprimir_arreglo(listaSueldos)
algoritmo_burbuja(listaSueldos)
imprimir_arreglo(listaSueldos)