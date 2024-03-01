class CarteiraDigital:
    def __init__(self):
        self.saldo_btc = 0.0
        self.saldo_dolar = 0.0
        self.invest_dolar = 0.0
        self.preco_medio = 0.0
        self.taxa_cambio_btc = 1.0
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
    
    def cotacao_btc(self, valor):
        self.taxa_cambio_btc = valor

    def comprar_btc(self, valor_em_dolar):
        quantidade_btc = valor_em_dolar / self.taxa_cambio_btc
        self.saldo_dolar -= valor_em_dolar
        self.saldo_btc += round(quantidade_btc, 8)
        self.invest_dolar += valor_em_dolar
        self.historico_transacoes.append(f'Compra de {quantidade_btc:.8f} BTC por ${valor_em_dolar:.2f}')

    def vender_btc(self, valor_em_dolar):
        quantidade_btc = valor_em_dolar / self.taxa_cambio_btc
        if quantidade_btc <= self.saldo_btc:
            self.saldo_dolar += valor_em_dolar
            self.saldo_btc -= round(quantidade_btc, 8)
            self.historico_transacoes.append(f'Venda de {quantidade_btc:.8f} BTC por ${valor_em_dolar:.2f}')
        else:
            return 'Saldo em BTC insuficiente para realizar a venda.'
        
    def atualizar_taxa_cambio_btc(self, nova_taxa):
        self.taxa_cambio_btc = nova_taxa

    def consultar_saldo(self):
        return {'saldo_dolar': self.saldo_dolar, 'saldo_btc': format(self.saldo_btc, '.8f').rstrip('0').rstrip('.')}

    def consultar_historico(self):
        return self.historico_transacoes.copy()

    def zerar_saldo_dolar(self):
        self.saldo_dolar = 0.0

    def zerar_saldo_btc(self):
        self.saldo_btc = 0.0

    def valor_btc_atual(self):
        return self.taxa_cambio_btc
    
    def valor_invest_dolar(self):
        return self.invest_dolar

    def consulta_preco_medio(self):
        preco_medio = self.taxa_cambio_btc
        if self.saldo_btc > 0:
            preco_medio = self.invest_dolar / self.saldo_btc
        return preco_medio
