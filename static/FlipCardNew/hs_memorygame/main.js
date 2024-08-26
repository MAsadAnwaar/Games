var imagens = []; // This will be dynamically populated

var caixasViradas = [];
var imagensViradas = [];
var caixasDesativadas = [];
var qtosCompletados;
var pontos;
var nivel = 1; // Track the current level

const pontuacaoAcertar = 20;
const pontuacaoErrar = -5;

function inicializar() {
    caixasViradas = [];
    imagensViradas = [];
    caixasDesativadas = [];
    
    qtosCompletados = 0;
    pontos = 0;

    document.getElementById("span-pontos").innerHTML = "Pontos: 0";
    document.getElementById("current-level").innerHTML = "Level: " + nivel;

    for (let i = 0; i < 32; i++) {
        document.getElementById("container" + i).style.opacity = '1';
        document.getElementById("carta" + i).style.transform = 'rotateY(0deg)';
        caixasDesativadas[i] = false;
    }
    
    // Populate the imagens array with card data from Django
    imagens = cardData.map(card => card.image_url);
    embaralharImagens();

    fetch('/get_new_background_image/')
        .then(response => response.json())
        .then(data => {
            if (data.background_image) {
                document.getElementById('principal').style.backgroundImage = `url(${data.background_image})`;
            } else {
                console.error('Background image not found');
            }
        })
        .catch(error => console.error('Error fetching new background image:', error));

    document.getElementById('botao').style.display = 'none'; // Hide the Next Level button initially
}

function embaralharImagens() {
    // Shuffle the imagens array
    for (let i = imagens.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [imagens[i], imagens[j]] = [imagens[j], imagens[i]];
    }
}

function caixaClick(objeto) {
    var idDoContainer = objeto.id.slice(9, 11);
    var imagemDaCaixa = imagens[idDoContainer];

    if (!caixasDesativadas[idDoContainer] && imagensViradas.length < 2) {
        document.getElementById("carta" + idDoContainer).style.transform = "rotateY(180deg)";
        document.getElementById("costa" + idDoContainer).style.backgroundImage = `url(${imagemDaCaixa})`;

        if (imagensViradas.length === 0) {
            imagensViradas.push(imagemDaCaixa);
            caixasViradas.push(idDoContainer);
            caixasDesativadas[caixasViradas[0]] = true;
            ajustarCursor();
        } else if (imagensViradas.length === 1) {
            imagensViradas.push(imagemDaCaixa);
            caixasViradas.push(idDoContainer);
            caixasDesativadas[caixasViradas[1]] = true;
            ajustarCursor();

            if (imagensViradas[0] === imagensViradas[1]) {
                qtosCompletados += 2;
                caixasDesativadas[caixasViradas[0]] = true;
                caixasDesativadas[caixasViradas[1]] = true;
                ajustarCursor();

                setTimeout(esconderImagens, 1000);

                if (qtosCompletados === 32) {
                    setTimeout(fimDeJogo, 1500);
                }
            } else {
                setTimeout(voltarImagensViradas, 1000);
            }
        }
    }
}

function voltarImagensViradas() {
    document.getElementById("carta" + caixasViradas[0]).style.transform = "rotateY(0deg)";
    document.getElementById("carta" + caixasViradas[1]).style.transform = "rotateY(0deg)";

    caixasDesativadas[caixasViradas[0]] = false;
    caixasDesativadas[caixasViradas[1]] = false;

    ajustarCursor();

    imagensViradas = [];
    caixasViradas = [];

    atualizarPontuacao(pontuacaoErrar);
}

function esconderImagens() {
    document.getElementById("container" + caixasViradas[0]).style.opacity = '0';
    document.getElementById("container" + caixasViradas[1]).style.opacity = '0';

    atualizarPontuacao(pontuacaoAcertar);

    setTimeout(ajustarEscondidas, 500);

    function ajustarEscondidas() {
        document.getElementById("carta" + caixasViradas[0]).style.transform = "rotateY(0deg)";
        document.getElementById("carta" + caixasViradas[1]).style.transform = "rotateY(0deg)";

        imagensViradas = [];
        caixasViradas = [];
    }
}

function atualizarPontuacao(valor) {
    pontos += valor;
    document.getElementById("span-pontos").innerHTML = "Pontos: " + pontos;
}

function ajustarCursor() {
    for (let i = 0; i < caixasDesativadas.length; i++) {
        if (caixasDesativadas[i]) {
            document.getElementById("container" + i).style.cursor = 'default';
        } else {
            document.getElementById("container" + i).style.cursor = 'pointer';
        }
    }
}

function fimDeJogo() {
    document.getElementById('botao').style.display = 'block'; // Show the Next Level button
    document.getElementById('botao').value = 'Next Level';
    document.getElementById('botao').onclick = function() {
        nivel++;
        inicializar(); // Restart the game with the new level
    };
}
