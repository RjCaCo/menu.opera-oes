import requests
from tabulate import tabulate

def obter_preco_bitcoin():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    resposta = requests.get(url)
    dados = resposta.json()
    preco_bitcoin = float(dados['price'])
    return preco_bitcoin

def calcular_operacao_compra(quantidade, preco_unitario):
    valor_total = quantidade / preco_unitario
    return valor_total

def main():
    total_quantidade_comprada = 0
    quantidade_btc_comprada_total = 0
    total_valor_gasto = 0
    historico_compras = []

    while True:
        #preco_unitario_bitcoin = obter_preco_bitcoin()
        preco_unitario_bitcoin = float(input("Preço unitário do Bitcoin em Dólares (0 para sair): "))
        quantidade_comprar = float(input("Quantidade de Bitcoin que deseja comprar em Dólares (0 para sair): "))
        
        if quantidade_comprar == 0:
            break
        
        total_quantidade_comprada += quantidade_comprar
        total_valor_gasto += quantidade_comprar
        quantidade_btc_comprada = quantidade_comprar / preco_unitario_bitcoin
        quantidade_btc_comprada_total += quantidade_btc_comprada
        preco_medio = total_valor_gasto / quantidade_btc_comprada_total if total_quantidade_comprada > 0 else 00
        historico_compras.append([quantidade_comprar, preco_unitario_bitcoin, total_valor_gasto, quantidade_btc_comprada_total, preco_medio])
    
    if quantidade_btc_comprada_total == 0:
        print("Nenhuma compra realizada.")
    else:
        headers = ["Quantidade Comprada", "Preço Unitário (USD)", "Valor Total (USD)", "Quantidade Total (BTC)", "Preço Médio (USD)"]
        print(tabulate(historico_compras, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    main()