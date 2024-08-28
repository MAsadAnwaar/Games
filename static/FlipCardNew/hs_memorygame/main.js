var imagens = [];
var caixasViradas = [];
var imagensViradas = [];
var caixasDesativadas = [];
var qtosCompletados;
var points;
var nivel; // Track the current level

const pontuacaoAcertar = 20;
const pontuacaoErrar = -5;

function inicializar() {
    nivel = parseInt(document.querySelector('meta[name="nivel"]').getAttribute('content')); // Get the current level from meta tag

    // Calculate the grid size based on the level
    const gridSizes = [12, 16, 20, 24, 28, 32]; // Represents 4x3, 4x4, 4x5, 4x6, 4x7, 4x8
    let numCards = gridSizes[Math.min(Math.floor((nivel - 1) / 2), gridSizes.length - 1)]; // Determine the grid size

    caixasViradas = [];
    imagensViradas = [];
    caixasDesativadas = [];
    
    qtosCompletados = 0;
    points = 0;

    document.getElementById("span-points").innerHTML = "Points: 0";
    document.getElementById("current-level").innerHTML = "Level: " + nivel;

    // Update grid container
    const gridContainer = document.getElementById("grid-container");
    gridContainer.innerHTML = ''; // Clear existing cards

    for (let i = 0; i < numCards; i++) {
        const section = document.createElement("section");
        section.id = "container" + i;
        section.onclick = () => caixaClick(section);

        const div = document.createElement("div");
        div.id = "carta" + i;

        const frente = document.createElement("figure");
        frente.id = "frente";

        const costa = document.createElement("figure");
        costa.id = "costa" + i;

        div.appendChild(frente);
        div.appendChild(costa);
        section.appendChild(div);

        gridContainer.appendChild(section);
    }

    // Populate the imagens array with card data from Django
    imagens = cardData.map(card => card.image_url);
    embaralharImagens();

    // Fetch the background image based on level
    document.getElementById('principal').style.backgroundImage = `url(${background_image})`;

    document.getElementById('botao').style.display = 'none'; // Hide the Next Level button initially
}

function goToNextLevel() {
    if (nivel < maxLevel) {
        window.location.href = `/hs_memorygame/?level=${nivel + 1}`;
    } else {
        alert("Congratulations! You've completed the game.");
    }
}


function embaralharImagens() {
    // Update the number of images based on the grid size
    let numImages = document.getElementById("grid-container").children.length;
    let selectedImages = randomSample(imagens, numImages / 2);
    let allImages = selectedImages.concat(selectedImages);
    
    // Shuffle the images
    for (let i = allImages.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [allImages[i], allImages[j]] = [allImages[j], allImages[i]];
    }
    
    for (let i = 0; i < allImages.length; i++) {
        document.getElementById("costa" + i).style.backgroundImage = `url(${allImages[i]})`;
    }
}

function caixaClick(objeto) {
    var idDoContainer = objeto.id.slice(9);
    var imagemDaCaixa = document.getElementById("costa" + idDoContainer).style.backgroundImage.slice(5, -2); // Extract the URL

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

                if (qtosCompletados === document.getElementById("grid-container").children.length) {
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
    points += valor;
    document.getElementById("span-points").innerHTML = "Points: " + points;
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
    document.getElementById('botao').onclick = goToNextLevel; // Set the click handler for the Next Level button
}

// Helper function to get random sample
function randomSample(array, size) {
    let shuffled = array.slice(0), i = array.length, min = i - size, temp, index;
    while (i-- > min) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
    }
    return shuffled.slice(min);
}

function goToNextLevel() {
    if (nivel < maxLevel) {
        window.location.href = `/hs_memorygame/?level=${nivel + 1}`;
    } else {
        alert("Congratulations! You've completed the game.");
    }
}
function openImage(element) {
    const modal = document.getElementById('image-modal');
    const fullImage = document.getElementById('full-image');
    fullImage.src = element.src;
    modal.style.display = "block";
}

function closeImage() {
    const modal = document.getElementById('image-modal');
    modal.style.display = "none";
}
