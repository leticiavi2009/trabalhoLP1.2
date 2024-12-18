def cardapio(nome_do_prato, valor, descricao, ingredientes):
    
def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Entre com o valor para {nome_variavel}: ')
    while valor_lido == '':
        print(f'O valor para {nome_variavel} não pode ser vazio!')
        valor_lido = input(f'Entre com o valor para {nome_variavel}: ')
    return valor_lido

def ler_parametro():
    nome_do_prato = ler_valor_nao_vazio('nome')
    valor = ler_valor_nao_vazio('valor')
    descricao = ler_valor_nao_vazio('descricao')
    ingredientes = ler_valor_nao_vazio('ingredientes')

    prato = {
        'nome': nome_do_prato,
        'valor': valor,
        'descricao': descricao,
        'ingredientes': ingredientes
    }

    return prato

def imprimir_prato(prato,):
    print(f"Nome:\t\t{prato,['nome']}")
    print(f"Valor:\t{prato,['valor']}")
    print(f"Descrição:\t\t{prato,['descricao']}")
    print(f"Ingredientes:\t\t{prato,['ingredientes']}")

meu_prato = ler_parametro()
meu_outro_prato = ler_parametro()
imprimir_prato(meu_bixinho)
imprimir_prato(meu_outro_bixinho)    
