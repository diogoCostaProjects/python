def create_item(item_list, item):
    item_list.append(item)
    print("Item adicionado com sucesso!")

def read_items(item_list):
    if not item_list:
        print("A lista está vazia.")
    else:
        print("Itens na lista:")
        for index, item in enumerate(item_list):
            print(f"{index + 1}. {item}")

def update_item(item_list, index, new_item):
    if index < 0 or index >= len(item_list):
        print("Índice inválido.")
    else:
        item_list[index] = new_item
        print("Item atualizado com sucesso!")

def delete_item(item_list, index):
    if index < 0 or index >= len(item_list):
        print("Índice inválido.")
    else:
        deleted_item = item_list.pop(index)
        print(f"Item '{deleted_item}' removido com sucesso!")

def escrever_arquivo(nome_arquivo, texto):
    if nome_arquivo == '' :
        nome_arquivo =  'lista_tarefas.txt'
        
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)

def ler_arquivo():
    with open('lista_tarefas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def converter_array_para_string(arr):
    return ' '.join(map(str, arr))

# Exemplo de uso:
# texto_para_escrever = "Este é um exemplo de texto para escrever em um arquivo."
# nome_do_arquivo = "exemplo.txt"
# escrever_arquivo(nome_do_arquivo, texto_para_escrever)

def main():
    items = []

    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Mostrar itens")
        print("3. Atualizar item")
        print("4. Deletar item")
        print("5. Gravar em arquivo")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            item = input("Digite o item que deseja adicionar: ")
            create_item(items, item)
        elif choice == "2":
            read_items(items)
        elif choice == "3":
            index = int(input("Digite o índice do item que deseja atualizar: ")) - 1
            new_item = input("Digite o novo valor do item: ")
            update_item(items, index, new_item)
        elif choice == "4":
            index = int(input("Digite o índice do item que deseja deletar: ")) - 1
            delete_item(items, index)
        elif choice == "5":
            print("Gravando em arquivo de texto...")
            result = converter_array_para_string(items)
            escrever_arquivo('', result)
            conteudo_arquivo = ler_arquivo()
            print('Conteúdo gravado')
            print(conteudo_arquivo)
            break
        elif choice == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
