// Função para atualizar a carteira
function atualizarCarteira() {
    fetch('/atualizar_carteira')
        .then(response => response.json())
        .then(data => {
            document.getElementById('saldo_dolar').innerText = data.saldo_dolar;
            document.getElementById('saldo_btc').innerText = data.saldo_btc;
        });
}

// Adiciona event listener para o input de depósito
document.getElementById('valor_deposito').addEventListener('change', function() {
    atualizarCarteira();
});

// Adiciona event listener para o input de saque
document.getElementById('valor_saque').addEventListener('change', function() {
    atualizarCarteira();
});

// Adiciona event listener para o input de compra de BTC
document.getElementById('valor_compra_btc').addEventListener('change', function() {
    atualizarCarteira();
});

// Adiciona event listener para o input de venda de BTC
document.getElementById('valor_venda_btc').addEventListener('change', function() {
    atualizarCarteira();
});

function consultarValorBTC() {
    fetch('/consultar_valor_btc_atual')
        .then(response => response.json())
        .then(data => {
            document.getElementById('valor_btc_atual').innerText = data.valor_btc;
        })
        .catch(error => {
            console.error("Erro ao consultar o valor atual do BTC:", error);
        });
}
consultarValorBTC(); // Consulta ao carregar a página
setInterval(consultarValorBTC, 11000);

document.getElementById('toggle-historico').addEventListener('click', function() {
    var historicoDiv = document.getElementById('historico');
    if (historicoDiv.style.display === 'none') {
        historicoDiv.style.display = 'block';
        this.innerText = 'Ocultar Histórico';
    } else {
        historicoDiv.style.display = 'none';
        this.innerText = 'Mostrar Histórico';
    }
});
