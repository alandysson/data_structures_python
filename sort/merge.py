def mergeSort(uma_lista):
    print("Splitting ", uma_lista)
    if len(uma_lista) > 1:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k] = esquerda[i]
                i = i+1
            else:
                uma_lista[k] = direita[j]
                j = j+1
                k = k+1
        while i < len(esquerda):
            uma_lista[k] = esquerda[i]
            i = i+1
            k = k+1
        while j < len(direita):
            uma_lista[k] = direita[j]
            j = j+1
            k = k+1
        print("Merging ", uma_lista)
