import requests
from tabulate import tabulate

def obter_preco_bitcoin():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    resposta = requests.get(url)
    dados = resposta.json()
    preco_bitcoin = float(dados['price'])
    return preco_bitcoin

def calcular_operacao_compra(quantidade, preco_unitario):
    valor_total = quantidade * preco_unitario
    return valor_total

def main():
    total_quantidade_comprada = 0
    total_valor_gasto = 0
    historico_compras = []

    while True:
        #preco_unitario_bitcoin = obter_preco_bitcoin()
        preco_unitario_bitcoin = float(input("Preço unitário do Bitcoin em Dólares: "))
        print(f"Preço atual do Bitcoin: ${preco_unitario_bitcoin:.2f}")
        
        quantidade_comprar = float(input("Quantidade de Bitcoin que deseja comprar (ou 0 para finalizar): "))
        
        if quantidade_comprar == 0:
            break
        
        total_quantidade_comprada += quantidade_comprar
        
        valor_total_compra = calcular_operacao_compra(quantidade_comprar, preco_unitario_bitcoin)
        total_valor_gasto += valor_total_compra
        
        preco_medio = total_valor_gasto / total_quantidade_comprada if total_quantidade_comprada > 0 else 0
        
        historico_compras.append([quantidade_comprar, preco_unitario_bitcoin, valor_total_compra, total_quantidade_comprada, preco_medio])
    
    if total_quantidade_comprada == 0:
        print("Nenhuma compra realizada.")
    else:
        headers = ["Quantidade Comprada", "Preço Unitário (USD)", "Valor Total (USD)", "Quantidade Total", "Preço Médio (USD)"]
        print(tabulate(historico_compras, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    main()