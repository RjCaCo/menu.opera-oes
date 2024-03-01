var historico = obter_historico_transacoes();

function atualizarCarteira() {
    fetch('/consultar_saldo')
        .then(response => response.json())
        .then(data => {
            document.querySelector('.saldo-dolar').innerHTML = '<i class="fas fa-dollar-sign"></i> Saldo em Dólar: $' + data.saldo_dolar;
            document.querySelector('.saldo-btc').innerHTML = '<i class="fab fa-bitcoin"></i> Saldo em BTC: ' + data.saldo_btc;
        })
        .catch(error => {
            console.error("Erro ao atualizar a carteira:", error);
        });
}

function consultarValorBTC() {
    fetch('/consultar_valor_btc_atual')
        .then(response => response.json())
        .then(data => {
            document.getElementById('valor_btc_atual').innerText = data.valor_btc;
        })
}
/* consultarValorBTC();
setInterval(consultarValorBTC, 5000); */

function obter_historico_transacoes() {
    var historico = localStorage.getItem('historico_transacoes');
    if (!historico) return [];

    return historico.map(function(transacaoString) {
        var tipo = transacaoString.split(' ')[0];
        var valor = parseFloat(transacaoString.match(/\$\d+\.\d+/)[0].substring(1));
        return {
            tipo: tipo,
            valor: valor
        };
    });
}

function adicionarTransacao(transacao) {
    adicionar_transacao_ao_historico(transacao);
}

function adicionar_transacao_ao_historico(transacao) {
    var historico = JSON.parse(localStorage.getItem('historico')) || [];
    historico.push(transacao);
    localStorage.setItem('historico', JSON.stringify(historico));
}

function toggleHistorico() {
    var historicoDiv = document.getElementById('historico');
    var historico = JSON.parse(localStorage.getItem('historico')) || [];
    if (historico.length > 0) {
        var historicoHTML = historico.map(function(transacao) {
            return '<p>' + transacao + '</p>';
        }).join('');

        historicoDiv.innerHTML = historicoHTML;
    } else {
        historicoDiv.innerHTML = '<p>Nenhuma operação realizada</p>';
    }

    if (historicoDiv.style.display === 'none')
        historicoDiv.style.display = 'block';
    else
        historicoDiv.style.display = 'none';
}

function limparLocalStorage() {
    localStorage.clear(); 
    location.reload();
}

function calcularPrecoMedioCompras() {
    var historico = JSON.parse(localStorage.getItem('historico')) || [];
    var total = 0;
    var numCompras = 0;

    historico.forEach(function(transacao) {
        if (transacao.tipo === 'Compra') {
            total += transacao.valor;
            numCompras++;
        }
    });

    if (numCompras > 0) {
        var precoMedio = total / numCompras;
        document.getElementById('preco-medio-compras').innerText = 'Preço médio de compra de BTC: $' + precoMedio.toFixed(2);
    } else {
        document.getElementById('preco-medio-compras').innerText = 'Nenhuma compra realizada ainda.';
    }
}

document.getElementById('toggle-historico').addEventListener('click', toggleHistorico);


document.getElementById('valor_deposito').addEventListener('change', () => {
    atualizarCarteira();
});

document.getElementById('valor_saque').addEventListener('change', () => {
    atualizarCarteira();
});

document.getElementById('valor_compra_btc').addEventListener('change', () => {
    atualizarCarteira();
});

document.getElementById('valor_venda_btc').addEventListener('change', () => {
    atualizarCarteira();
});