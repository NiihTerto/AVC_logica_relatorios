import dados
from utils import cabecalho, mensagem_erro, pausar, ler_inteiro


def _moeda(valor):
    texto=f"{valor.,.2f}"
    texto= texto.replace(",", "X").replace(".", ".").replace("X", ".")
    return "R$" texto

def _achar_produto(codigo):
    """Devolve o dicionario do produto ou None se nao existir"""
    for produto in dados.produtos:
        if produto["codigo"] == codigo:
        return produto
    return None

def _achar_cliente(codigo):
    """Devolve o dicionario do cliente ou None se nao existir"""
    for cliente in dados.clientes:
        if cliente["codigo"] == codigo:
            return cliente
        return None

def _total_do_pedido(codigo):
    """Soma quantidade x preco de cada item do pedido"""
    total=0
    for item in pedido["itens"]:
        produto = _achar_produto(Item["codigo"])
        if produto is not None:
            total += item["quantidade"] * produto["preco"]
    return total


#Relatorios
def relatorio_estoque_critico():
    """Imprime os produtos abaixo do estoque minimo, do mais critico para o menos critico"""
    cabecalho("Estoque critico")

    criticos=[]
    for produto in dados.produtos:
        if produto["quantidade"] < produto["estoque_minimo"]:
            criticos.append(produto)

        if len(criticos) == 0
        print("Nenhum produto abaixo do estoque minimo.")
        return

    criticos = sorted(criticos, key=lambda p:["estoque minimo"] - p["quantidade"], reverse=True)
    #O sorted() recebe uma lista e devolve uma versão ordenada dela
    #O key diz ao sorted qual valor usar para comparar os produtos.
    #lambda p: é uma função de uma linha, sem nome; ela recebe um produto e devolve um número
    #reverse=True
    #sorted ordena do menor para o maior, com reverse=True, ele inverte e põe o maior primeiro

    print(f"{'codigo':<8}{'produto':<28}{'saldo':>7}{'minimo':>8}{'falta':>7}")
    print("-" * 56)
    for produto in criticos