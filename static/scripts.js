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

// Função para obter o histórico de transações armazenado no localStorage
function obter_historico_transacoes() {
    // Verifica se há histórico armazenado no localStorage
    var historico = localStorage.getItem('historico_transacoes');
    
    // Se não houver histórico armazenado, retorna um array vazio
    if (!historico) {
        return [];
    }
    
    // Se houver histórico armazenado, converte a string JSON para um array e retorna
    return JSON.parse(historico);
}

function adicionarTransacao(transacao) {
    adicionar_transacao_ao_historico(transacao);
}

function adicionar_transacao_ao_historico(transacao) {
    // Obtém o histórico atual do localStorage
    var historico = JSON.parse(localStorage.getItem('historico')) || [];

    // Adiciona a nova transação ao histórico
    historico.push(transacao);

    // Atualiza o histórico no localStorage
    localStorage.setItem('historico', JSON.stringify(historico));
}

// Exemplo de uso:
var historico = obter_historico_transacoes();
console.log(historico); // Mostra o histórico de transações recuperado do localStorage

function toggleHistorico() {
    var historicoDiv = document.getElementById('historico');
    var historico = JSON.parse(localStorage.getItem('historico')) || [];

    // Se houver transações no histórico, exibe-as
    if (historico.length > 0) {
        var historicoHTML = historico.map(function(transacao) {
            return '<p>' + transacao + '</p>';
        }).join('');

        historicoDiv.innerHTML = historicoHTML;
    } else {
        // Se não houver transações, exibe uma mensagem indicando isso
        historicoDiv.innerHTML = '<p>Nenhuma operação realizada</p>';
    }

    // Alterna a visibilidade do histórico
    if (historicoDiv.style.display === 'none') {
        historicoDiv.style.display = 'block';
    } else {
        historicoDiv.style.display = 'none';
    }
}


document.getElementById('toggle-historico').addEventListener('click', toggleHistorico);