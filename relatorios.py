import dados
from utils import cabecalho, mensagem_erro, pausar, ler_inteiro


def _moeda(valor):
<<<<<<< HEAD
    texto=f"{valor:,.2f}"
    texto= texto.replace(",", "X").replace(".", ".").replace("X", ".")
    return "R$" + texto
=======
    texto=f"{valor.,.2f}"
    texto= texto.replace(",", "X").replace(".", ".").replace("X", ".")
    return "R$" texto
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c

def _achar_produto(codigo):
    """Devolve o dicionario do produto ou None se nao existir"""
    for produto in dados.produtos:
        if produto["codigo"] == codigo:
<<<<<<< HEAD
            return produto
=======
        return produto
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c
    return None

def _achar_cliente(codigo):
    """Devolve o dicionario do cliente ou None se nao existir"""
    for cliente in dados.clientes:
        if cliente["codigo"] == codigo:
            return cliente
        return None

def _total_do_pedido(codigo):
<<<<<<< HEAD
    """Soma qtd x preco de cada item do pedido"""
=======
    """Soma quantidade x preco de cada item do pedido"""
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c
    total=0
    for item in pedido["itens"]:
        produto = _achar_produto(Item["codigo"])
        if produto is not None:
<<<<<<< HEAD
            total += item["qtd"] * produto["preco"]
=======
            total += item["quantidade"] * produto["preco"]
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c
    return total


#Relatorios
def relatorio_estoque_critico():
    """Imprime os produtos abaixo do estoque minimo, do mais critico para o menos critico"""
    cabecalho("Estoque critico")

    criticos=[]
    for produto in dados.produtos:
<<<<<<< HEAD
        if produto["qtd"] < produto["estoque_minimo"]:
            criticos.append(produto)

        if len(criticos) == 0:
            print("Nenhum produto abaixo do estoque minimo.")
        return

    criticos = sorted(criticos, key=lambda p:["estoque minimo"] - p["qtd"], reverse=True)
    #O sorted() recebe uma lista e devolve uma versão ordenada dela
    #O key diz ao sorted qual valor usar para comparar os produtos.
    #lambda p: é uma função de uma linha, sem nome; ela recebe um produto e devolve um número
=======
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
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c
    #sorted ordena do menor para o maior, com reverse=True, ele inverte e põe o maior primeiro

    print(f"{'codigo':<8}{'produto':<28}{'saldo':>7}{'minimo':>8}{'falta':>7}")
    print("-" * 56)
<<<<<<< HEAD
    for produto in criticos:
        falta = produto["estoque_minimo"] - produto["quantidade"]
        print(f"{produto['codigo']:<8}{produto['nome']:<26}"
              f"{produto['qtd']:>7}{produto['estoque_minimo']:>8}{falta:>7}")
    print("-") * 56
    print(f"Total de produtos em situacao critica: {len(criticos)}")


def relatorio_por_giro():
     """Conta quanto de cada produto saiu nos pedidos e imprime 
     do mais vendido para o menos vendido. Pedidos cancelados nao contam como venda"""
     cabecalho("Giro de produtos")

     vendido = {}
     for pedido in dados.pedidos:
         if pedido["status"] == "cancelado":
             continue
         for item in pedido["itens"]:
             codigo = item["codigo"]
             vendido[codigo] - vendido.get(codigo, 0) + item["qtd"]

    if len(vendido) == 0:
        print("Nenhum produto foi vendido ainda.")
        return

print(f"{'#':<4}{'Codigo':<8}{'Produto':<26}{'Qtd vendida':>12}")
print("-" * 50)
posicao = 1
for codigo, qtd in ranking:
    produto = _achar_produto(codigo)
    nome = produto["nome"] if produto is not None else "(produto removido)"
    print(f"{posicao:<4}{codigo:<8}{nome:<26}{qtd:>12}")
    posicao += 1


def relatorio_pedidos_por_cliente(codigo_cliente):
    """Imprime todos os pedidos de um cliente e o valor de cada um."""
    cabecalho("Pedidos por cliente")

    cliente = _achar_cliente(codigo_cliente):
    if cliente is None:
        mensagem_erro("Cliente nao encontrado.")
        return

    print(f"Cliente:{cliente['nome']}) ({cliente['tipo']} - {cliente['bairro']})")
    print()

    pedidos_do_cliente = []
    for pedido in dados.pedidos:
        if pedido["cliente"] == codigo_cliente:
            pedidos_do_cliente.append(pedido)

    if len(pedidos_do_cliente) == 0:
        print("Esse cliente ainda nao tem pedidos.")
        return
=======
    for produto in criticos
>>>>>>> c21ca2e3acae8a37dc7192d8bbf033b9b997fa1c
