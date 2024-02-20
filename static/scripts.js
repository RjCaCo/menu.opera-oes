// Exemplo de uso:
var historico = obter_historico_transacoes();

// Função para atualizar a carteira
function atualizarCarteira(operacao) {
    if(operacao == 'compra') {
        
    }
    fetch('/atualizar_carteira')
        .then(response => response.json())
        .then(data => {
            document.getElementById('saldo_dolar').innerText = data.saldo_dolar;
            document.getElementById('saldo_btc').innerText = data.saldo_btc;
        });
}

// Adiciona event listener para o input de depósito
document.getElementById('valor_deposito').addEventListener('change', function() {
    atualizarCarteira('deposito');
});

// Adiciona event listener para o input de saque
document.getElementById('valor_saque').addEventListener('change', function() {
    atualizarCarteira('saque');
});

// Adiciona event listener para o input de compra de BTC
document.getElementById('valor_compra_btc').addEventListener('change', function() {
    console.log('estou comprando BTC');
    
    atualizarCarteira('compra');
});

// Adiciona event listener para o input de venda de BTC
document.getElementById('valor_venda_btc').addEventListener('change', function() {
    atualizarCarteira('venda');
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
setInterval(consultarValorBTC, 5000);

// Função para obter o histórico de transações armazenado no localStorage
/* function obter_historico_transacoes() {
    // Verifica se há histórico armazenado no localStorage
    var historico = localStorage.getItem('historico_transacoes');
    
    // Se não houver histórico armazenado, retorna um array vazio
    if (!historico) {
        return [];
    }
    
    // Se houver histórico armazenado, converte a string JSON para um array e retorna
    return JSON.parse(historico);
} */

function obter_historico_transacoes() {
    // Verifica se há histórico armazenado no localStorage
    var historico = localStorage.getItem('historico_transacoes');
    
    // Se não houver histórico armazenado, retorna um array vazio
    if (!historico) {
        return [];
    }
    
    // Se houver histórico armazenado, converte a string JSON para um array de objetos e retorna
    return historico.map(function(transacaoString) {
        var tipo = transacaoString.split(' ')[0]; // Obtém o tipo de transação (Depósito, Saque, Compra, Venda)
        var valor = parseFloat(transacaoString.match(/\$\d+\.\d+/)[0].substring(1)); // Obtém o valor da transação

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
    // Obtém o histórico atual do localStorage
    var historico = JSON.parse(localStorage.getItem('historico')) || [];

    // Adiciona a nova transação ao histórico
    historico.push(transacao);

    // Atualiza o histórico no localStorage
    localStorage.setItem('historico', JSON.stringify(historico));
}

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

/* function preco_medio() {
    var historico = JSON.parse(localStorage.getItem('historico'))
    var numeros = [];

    historico.forEach(function(texto) {
        var matches = texto.match(/\$(\d+)/);
        if (matches && matches[1]) {
            numeros.push(parseInt(matches[1]));
        }
    });
    console.log(numeros); 
}
preco_medio();
setInterval(preco_medio, 3000); */

function preco_medio() {
    // Verifica se há histórico armazenado no localStorage
    var historico = JSON.parse(localStorage.getItem('historico_transacoes'));
    if (!historico) {
        console.log("Nenhum histórico de transações encontrado");
        return;
    }

    var numeros = [];

    historico.forEach(function(texto) {
        var matches = texto.match(/\$(\d+)/);
        if (matches && matches[1]) {
            numeros.push(parseInt(matches[1]));
        }
    });
    console.log(numeros); 
}

preco_medio();
setInterval(preco_medio, 3000);

document.getElementById('toggle-historico').addEventListener('click', toggleHistorico);

