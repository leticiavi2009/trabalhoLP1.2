#def cardapio(nome do prato, preço, descricao, ingredientes):             #esses f' são só uma maneira diferente de misturar variável e texto
import json

lista=[]
def ler_valor_nao_vazio(nome_variavel):                                   #o "nome_variavel" aqui é o que a pessoa informou, só que nessa função ela tem esse nome
    valor_lido = input(f'Entre com o valor para {nome_variavel}: ')       #entra com o valor da variável
    while valor_lido == '':
        print(f'O valor para {nome_variavel} não pode ser vazio!')        #enquanto o valor é vazio o código não anda
        valor_lido = input(f'Entre com o valor para {nome_variavel}: ')
    return valor_lido                                                     #retorna o valor que ele leu

def incluir():
    quantidade = int(input("Informe quantos pratos você deseja cadastrar: \n"))       #limita a quantidade de pratos que você quer
    for i in range(quantidade):                                                         
        meu_prato = ler_prato()
        lista.append(meu_prato)
        imprimir_cardapio(lista)
        salvar_json(lista)

def menu():
    while True:
        menu1 = int(input("Você deseja(digite o número):\n1-Incluir\n2-Consultar\n3-Modificar\n4-Excluir\n0-Sair\n"))
        if menu1 == 0:
            break
        if menu1 == 1:
            incluir()
        if menu1 == 2:
            if len(lista) == 0:
                print("Cardápio vazio!")
            else:
                imprimir_cardapio(lista)
        if menu1 == 3:
            modificar()
        if menu1 == 4:
            excluir_prato()
    
def ler_prato():                                                          #a função só irá ler as informações, é vazio porque
    nome_do_prato = ler_valor_nao_vazio('nome')                           #a variável "nome_do_prato" vai chmar a função "ler_valor_nao_vazio" com 
    preco = ler_valor_nao_vazio('preço')                                  #o parâmetro "nome" e assim por diante
    descricao = ler_valor_nao_vazio('descrição')
    ingredientes = ler_valor_nao_vazio('ingredientes')

    prato = {
        'nome': nome_do_prato,
        'preco': preco,                                                 #variável(objeto) "prato" com outras variáveis dentro 'nome' que possui o valor "nome_do_prato", 
        'descricao': descricao,                                         #essa é a definição de dicionário(j.son)
        'ingredientes': ingredientes
    }

    return prato    
                                                                            #retorna um dicionário chamado "prato" com outras variáveis dentro
def modificar():
    modifica = int(input("Digite o número do prato que deseja modificar: "))
    lista.pop(modifica - 1)
    

    

def imprimir_prato(prato):                                               
    print(f"Nome:\t\t\t{prato['nome']}")
    print(f"Preço:\t\t\t{prato['preco']}")
    print(f"Descrição:\t\t{prato['descricao']}")
    print(f"Ingredientes:\t\t{prato['ingredientes']}\n")

def imprimir_cardapio(cardapio): 
    print("=======CARDÁPIO========")                                    #só pra dar um tchan ;)
    for i, prato in enumerate(cardapio):                                #é pra enumerar automaticamente
        print(f"========== {i+1} ==========")
        imprimir_prato(prato)
        print("=========================")
def excluir_prato():
    prato_excluido = int(input('Qual posição do prato deseja excluir?(digite os números): \n'))
    lista.pop(prato_excluido - 1)
    imprimir_cardapio(lista)
    salvar_json(lista)

def salvar_json(lista):
    with open("cardapio.json","w") as meu_arquivo:           #cardapio.json é o arquivo
        lista_json = json.dumps(lista, indent = 4)
        meu_arquivo.write(lista_json)
   
        

menu()