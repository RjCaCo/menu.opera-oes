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
        return self.carteira.consulta_preco_medio()
    
    def valor_cotacao(self, valor):
        return self.carteira.cotacao_btc(valor)
    
    def valor_btc_atual(self):
        return self.carteira.valor_btc_atual()
    
    def valor_invest_dolar(self):
        return self.carteira.valor_invest_dolar()


