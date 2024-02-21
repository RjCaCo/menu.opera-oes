import requests
import threading
from models.carteira_model import CarteiraDigital
from controllers.carteira_controller import CarteiraController
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='views')

carteira = CarteiraDigital()
controller = CarteiraController(carteira)

@app.route('/')
def index():
    saldo = controller.consultar_saldo()
    historico = controller.consultar_historico()
    return render_template('carteira_template.html', 
                           saldo_dolar=saldo['saldo_dolar'], 
                           saldo_btc=saldo['saldo_btc'], 
                           historico=historico)

@app.route('/deposito', methods=['POST'])
def deposito():
    valor_deposito = float(request.form['valor_deposito'])
    controller.realizar_deposito(valor_deposito)
    return redirect(url_for('index'))

@app.route('/saque', methods=['POST'])
def saque():
    valor_saque = float(request.form['valor_saque'])
    controller.realizar_saque(valor_saque)
    return redirect(url_for('index'))

@app.route('/comprar_btc', methods=['POST'])
def comprar_btc():
    valor_compra_btc = float(request.form['valor_compra_btc'])
    controller.realizar_compra_btc(valor_compra_btc)
    return redirect(url_for('index'))


@app.route('/vender_btc', methods=['POST'])
def vender_btc():
    valor_venda_btc = float(request.form['valor_venda_btc'])
    controller.realizar_venda_btc(valor_venda_btc)
    return redirect(url_for('index'))

@app.route('/atualizar_carteira')
def atualizar_carteira():
    return redirect(url_for('index'))

@app.route('/consultar_saldo', methods=['GET'])
def consultar_saldo():
    saldo = controller.consultar_saldo()
    return jsonify(saldo)

@app.route('/consultar_valor_btc_atual')
def consultar_valor_btc_atual():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        data = response.json()
        btc_price_usd = float(data["price"])
        carteira.atualizar_taxa_cambio_btc(btc_price_usd)
        return jsonify({'valor_btc': btc_price_usd})
    except Exception as e:
        print(f"Erro ao consultar o valor atual do BTC: {e}")
        return jsonify({'valor_btc': 'Erro'})
    
""" def atualizar_taxa_cambio_btc_periodicamente():
    try:
        nova_taxa_btc = 55000.0
        carteira.atualizar_taxa_cambio_btc(nova_taxa_btc)
        threading.Timer(5.0, atualizar_taxa_cambio_btc_periodicamente).start()
    except Exception as e:
        print(f"Erro ao atualizar a taxa de câmbio do BTC: {e}")
atualizar_taxa_cambio_btc_periodicamente() """

@app.route('/zerar_saldos')
def zerar_saldos():
    carteira.zerar_saldo_dolar()
    carteira.zerar_saldo_btc()
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run(debug=True)
