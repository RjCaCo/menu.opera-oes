import requests
from models.carteira_model import CarteiraDigital
from controllers.carteira_controller import CarteiraController
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='views')

# Configuração da carteira
carteira = CarteiraDigital()
controller = CarteiraController(carteira)

# Rota > página inicial
@app.route('/')
def index():
    saldo = controller.consultar_saldo()
    historico = controller.consultar_historico()
    return render_template('carteira_template.html', saldo_dolar=saldo['saldo_dolar'], saldo_btc=saldo['saldo_btc'], historico=historico)

# Rota > depósito em dólar
@app.route('/deposito', methods=['POST'])
def deposito():
    valor_deposito = float(request.form['valor_deposito'])
    controller.realizar_deposito(valor_deposito)
    return redirect(url_for('index'))

# Rota > saque em dólar
@app.route('/saque', methods=['POST'])
def saque():
    valor_saque = float(request.form['valor_saque'])
    controller.realizar_saque(valor_saque)
    return redirect(url_for('index'))

# Rota > compra de BTC
@app.route('/comprar_btc', methods=['POST'])
def comprar_btc():
    valor_compra_btc = float(request.form['valor_compra_btc'])
    controller.realizar_compra_btc(valor_compra_btc)
    return redirect(url_for('index'))

# Rota > venda de BTC
@app.route('/vender_btc', methods=['POST'])
def vender_btc():
    valor_venda_btc = float(request.form['valor_venda_btc'])
    controller.realizar_venda_btc(valor_venda_btc)
    return redirect(url_for('index'))

# Rota > atualizar a carteira
@app.route('/atualizar_carteira')
def atualizar_carteira():
    return redirect(url_for('index'))

# Rota para consultar o valor atual do BTC
@app.route('/consultar_valor_btc_atual')
def consultar_valor_btc_atual():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        data = response.json()
        btc_price_usd = float(data["price"])
        return jsonify({'valor_btc': btc_price_usd})
    except Exception as e:
        print(f"Erro ao consultar o valor atual do BTC: {e}")
        return jsonify({'valor_btc': 'Erro'})


if __name__ == '__main__':
    app.run(debug=True)
