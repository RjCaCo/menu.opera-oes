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
