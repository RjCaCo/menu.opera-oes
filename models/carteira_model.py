class CarteiraDigital:
    def __init__(self):
        self.saldo_dolar = 0.0
        self.saldo_btc = 0.0
        self.taxa_cambio_btc = 50000.0
        self.historico_transacoes = []

    def deposito(self, valor):
        self.saldo_dolar += valor
        self.historico_transacoes.append(f'Depósito de ${valor:.2f}')

    def saque(self, valor):
        if valor <= self.saldo_dolar:
            self.saldo_dolar -= valor
            self.historico_transacoes.append(f'Saque de ${valor:.2f}')
        else:
            return 'Saldo insuficiente para realizar o saque.'

    def comprar_btc(self, valor_em_dolar):
        quantidade_btc = valor_em_dolar / self.taxa_cambio_btc
        self.saldo_dolar -= valor_em_dolar
        self.saldo_btc += quantidade_btc
        self.historico_transacoes.append(f'Compra de {quantidade_btc:.8f} BTC por ${valor_em_dolar:.2f}')

    def vender_btc(self, valor_em_dolar):
        quantidade_btc = valor_em_dolar / self.taxa_cambio_btc
        if quantidade_btc <= self.saldo_btc:
            self.saldo_dolar += valor_em_dolar
            self.saldo_btc -= quantidade_btc
            self.historico_transacoes.append(f'Venda de {quantidade_btc:.8f} BTC por ${valor_em_dolar:.2f}')
        else:
            return 'Saldo em BTC insuficiente para realizar a venda.'

    def consultar_saldo(self):
        return {'saldo_dolar': self.saldo_dolar, 'saldo_btc': self.saldo_btc}

    def consultar_historico(self):
        return self.historico_transacoes.copy()
