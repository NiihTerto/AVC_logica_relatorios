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
    