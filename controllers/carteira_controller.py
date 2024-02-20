class CarteiraController:
    def __init__(self, carteira):
        self.carteira = carteira

    def realizar_deposito(self, valor):
        self.carteira.deposito(valor)

    def realizar_saque(self, valor):
        return self.carteira.saque(valor)

    def realizar_compra_btc(self, valor_em_dolar):
        self.carteira.comprar_btc(valor_em_dolar)

    def realizar_venda_btc(self, valor_em_dolar):
        return self.carteira.vender_btc(valor_em_dolar)

    def consultar_saldo(self):
        return self.carteira.consultar_saldo()

    def consultar_historico(self):
        return self.carteira.consultar_historico()
    
    def preco_medio(self):
        historico = self.carteira.consultar_historico()
        total_compras = 0
        total_vendas = 0
        quantidade_compras = 0
        quantidade_vendas = 0

        for transacao in historico:
            if transacao['tipo'].startswith('Compra'):
                total_compras += transacao['valor']
                quantidade_compras += 1
            elif transacao['tipo'].startswith('Venda'):
                total_vendas += transacao['valor']
                quantidade_vendas += 1

        if quantidade_compras == 0:
            preco_medio_compras = 0
        else:
            preco_medio_compras = total_compras / quantidade_compras

        if quantidade_vendas == 0:
            preco_medio_vendas = 0
        else:
            preco_medio_vendas = total_vendas / quantidade_vendas

        return (preco_medio_compras, preco_medio_vendas)

        #return (10000, 20000)
