# relatorios.py - relatorios gerenciais do SIGEP
# Este modulo so LE os dados de dados.py. Nunca altera nenhuma lista.
import dados
from utils import cabecalho, mensagem_erro, pausar, ler_inteiro


# Funcoes auxiliares (comecam com _ = uso interno deste arquivo)
# Percorrem dados.py direto, assim este modulo nao depende dos
# modulos produtos.py, clientes.py e pedidos.py para funcionar.
def _moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


def _achar_produto(codigo):
    """Devolve o dicionario do produto, ou None se nao existir."""
    for produto in dados.produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def _achar_cliente(codigo):
    """Devolve o dicionario do cliente, ou None se nao existir."""
    for cliente in dados.clientes:
        if cliente["codigo"] == codigo:
            return cliente
    return None


def _total_do_pedido(pedido):
    """Soma qtd x preco de cada item do pedido.
    Item cujo produto foi removido do cadastro nao entra na soma."""
    total = 0
    for item in pedido["itens"]:
        produto = _achar_produto(item["codigo"])
        if produto is not None:
            total += item["qtd"] * produto["preco"]
    return total


# Relatorios
def relatorio_estoque_critico():
    """Imprime os produtos abaixo do estoque minimo,
    do mais critico para o menos critico."""
    cabecalho("Estoque critico")

    criticos = []
    for produto in dados.produtos:
        if produto["quantidade"] < produto["estoque_minimo"]:
            criticos.append(produto)

    if len(criticos) == 0:
        print("Nenhum produto abaixo do estoque minimo.")
        return

    criticos = sorted(criticos,
                      key=lambda p: p["estoque_minimo"] - p["quantidade"],
                      reverse=True)

    print(f"{'Codigo':<8}{'Produto':<26}{'Saldo':>7}{'Minimo':>8}{'Falta':>7}")
    print("-" * 56)
    for produto in criticos:
        falta = produto["estoque_minimo"] - produto["quantidade"]
        print(f"{produto['codigo']:<8}{produto['nome']:<26}"
              f"{produto['quantidade']:>7}{produto['estoque_minimo']:>8}{falta:>7}")
    print("-" * 56)
    print(f"Total de produtos em situacao critica: {len(criticos)}")


def relatorio_por_giro():
    """Conta quanto de cada produto saiu nos pedidos e imprime
    do mais vendido para o menos vendido. Use sorted().
    Pedidos cancelados nao contam como venda."""
    cabecalho("Giro de produtos")

    vendido = {}
    for pedido in dados.pedidos:
        if pedido["status"] == "cancelado":
            continue
        for item in pedido["itens"]:
            codigo = item["codigo"]
            vendido[codigo] = vendido.get(codigo, 0) + item["qtd"]

    if len(vendido) == 0:
        print("Nenhum produto foi vendido ainda.")
        return

    # vendido.items() gera pares (codigo, qtd). Ordenamos pela qtd (posicao 1).
    ranking = sorted(vendido.items(), key=lambda par: par[1], reverse=True)

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

    cliente = _achar_cliente(codigo_cliente)
    if cliente is None:
        mensagem_erro("Cliente nao encontrado.")
        return

    print(f"Cliente: {cliente['nome']} ({cliente['tipo']} - {cliente['bairro']})")
    print()

    pedidos_do_cliente = []
    for pedido in dados.pedidos:
        if pedido["cliente"] == codigo_cliente:
            pedidos_do_cliente.append(pedido)

    if len(pedidos_do_cliente) == 0:
        print("Este cliente ainda nao tem pedidos.")
        return

    print(f""