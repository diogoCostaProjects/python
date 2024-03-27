import numpy as np

# Criando um array unidimensional
arr1 = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:")
print(arr1)

# Criando um array bidimensional
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray bidimensional:")
print(arr2)

# Acessando elementos do array
print("\nElemento na posição (0, 0):", arr2[0, 0])
print("Última linha do array bidimensional:", arr2[-1])

# Operações matemáticas com arrays
arr3 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
soma = arr2 + arr3
print("\nSoma dos arrays:")
print(soma)

# Transposição de um array
transposto = arr2.T
print("\nTransposto do array bidimensional:")
print(transposto)

# Operações es
