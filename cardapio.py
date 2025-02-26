#def cardapio(nome do prato, preço, descricao, ingredientes):           
import json

#o "nome_variavel" aqui é o que a pessoa informou, só que nessa função ela tem esse nome
def ler_valor_nao_vazio(nome_variavel):
    #entra com o valor da variável                                   
    valor_lido = input(f'Entre com o valor para {nome_variavel}: ')       
    while valor_lido == '':
        #esses f' são só uma maneira diferente de misturar variável e texto
        #enquanto o valor é vazio o código não anda
        print(f'O valor para {nome_variavel} não pode ser vazio!')        
        valor_lido = input(f'Entre com o valor para {nome_variavel}: ')
    #retorna o valor que ele leu
    return valor_lido                                                    

def incluir():
    #limita a quantidade de pratos que você quer
    quantidade = int(input("Informe quantos pratos você deseja cadastrar: \n"))      
    for i in range(quantidade):                                                         
        meu_prato = ler_prato()
        lista.append(meu_prato)
        imprimir_cardapio(lista)
        salvar_json(lista)

def menu():
    salvar_json(lista)
    print("--------Seja bem-vindo ao nosso site de restaurantes!--------")
    while True:
        menu1 = int(input("Você deseja(digite o número):\n1-Incluir\n2-Consultar\n3-Modificar\n4-Excluir\n0-Sair\n"))
        if menu1 == 0:
            if len(lista)>0:
                print("\nEsse é o seu cardápio final:")
                imprimir_cardapio(lista)
                break
            elif len(lista) == 0:
                print("Sem cardápio final!")
                break

        if menu1 == 1:
            incluir()
        if menu1 == 2:
            if len(lista) == 0:
                print("Cardápio vazio!")
            else:
                imprimir_cardapio(lista)
        if menu1 == 3:
            if len(lista) == 0:
                print("Você precisa de pelo menos 1 prato para poder modificar.")
            else:
                modificar()
        if menu1 == 4:
            if len(lista) == 0:
                print("Você precisa de pelo menos 1 prato para poder excluir.")
            else:
                excluir_prato()
    
#a função só irá ler as informações, é vazio porque a variável "nome_do_prato" vai chamar a função "ler_valor_nao_vazio" com
#o parâmetro "nome" e assim por diante
def ler_prato():                                                          
    nome_do_prato = ler_valor_nao_vazio('nome')                          
    preco = ler_valor_nao_vazio('preço')                                 
    descricao = ler_valor_nao_vazio('descrição')
    ingredientes = ler_valor_nao_vazio('ingredientes')

    #variável(objeto) "prato" com outras variáveis dentro 'nome' que possui o valor "nome_do_prato", essa é a definição de dicionário(j.son)
    prato = {
        'nome': nome_do_prato,
        'preco': preco,                                                
        'descricao': descricao,                                         
        'ingredientes': ingredientes
    }

    #retorna um dicionário chamado "prato" com outras variáveis dentro
    return prato

def modificar():
    modifica = int(input("Digite o número do prato que deseja modificar: "))
    # .pop exclui uma posição da lista 
    lista.pop(modifica - 1)
    for i in range(1):
        modificado = ler_prato()
        # .insert pega a posição da lista desejada e coloca o que o carinha digitou, usa-se dois parâmetros
        lista.insert(modifica - 1,modificado)
        imprimir_cardapio(lista)
        salvar_json(lista)
    
def imprimir_prato(prato):                                               
    print(f"---Nome:\t\t\t{prato['nome']}")
    print(f"---Preço:\t\t\t{prato['preco']}")
    print(f"---Descrição:\t\t\t{prato['descricao']}")
    print(f"---Ingredientes:\t\t{prato['ingredientes']}\n")

def imprimir_cardapio(cardapio):
    #só pra dar um tchan ;)
    print("°°°°°°CARDÁPIO°°°°°°°°")
    #é pra enumerar automaticamente
    for i, prato in enumerate(cardapio):                               
        print(f"========== {i + 1} ==========")
        imprimir_prato(prato)
        print("=========================")
        
def excluir_prato():
    prato_excluido = int(input('Qual posição do prato deseja excluir?(digite os números): \n'))
    lista.pop(prato_excluido - 1)
    imprimir_cardapio(lista)
    salvar_json(lista)

def salvar_json(lista):
    #cardapio.json é o arquivo
    with open("cardapio.json","w") as meu_arquivo:
        # "dumps" formata o dicionário como json tring          
        lista_json = json.dumps(lista, indent = 4)
        # "write" salva o conteúdo string no arquivo
        meu_arquivo.write(lista_json)
   
def ler_json():
    #"with" abre um arquivo e depois fecha ele, quando roda o open
    with open("cardapio.json", "r") as meu_arquivo:          
        #"load" é leia
        lista_json = json.load(meu_arquivo)                 
    return lista_json

lista = ler_json()
menu()
