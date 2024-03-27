# fruits = ["banana", "maçã", "morango"]
# # fruits.remove("banana")
# # fruits.append("banana")
# # fruits.append("melancia")
# # fruits.pop(1)
# for fruit in fruits:
#     print(fruit)
# num = input("Digite um número: ")
i = 0
valores = []

while(i<5):
    valores.append(input("Digite um número: "))
    i = i+1
print(f"O maior valor que você digitou foi:  {max(valores)}")