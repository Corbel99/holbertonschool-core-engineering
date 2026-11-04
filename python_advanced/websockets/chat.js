// Ouvre une connexion Websocket vers le serveur Python (Uvicorn, route /ws)
const socket = new WebSocket("ws://localhost:8000/ws");

// Quand la connexion s'ouvre, affiche un texte dans la console
socket.onopen = () => {
  console.log("Le grimoire s'éveille");
};

// Retrouve dans la page le champs de texte et le bouton, grâce à leur id
const input = document.getElementById("message-input");
const button = document.getElementById("send-button");
// Retrouve dans la page la zone du parchemin, où s'affichent les messages
const parchment = document.getElementById("messages")

function writeLine(text, kind) {
  // Fabrique un nouveau paragraphe vide
    const line = document.createElement("p");
    // Écrit le texte reçu en paramètre sur la ligne
    line.textContent = text;
    // Donne a la ligne sa classe : "sent" ou "received"
    line.className = kind;
    // Colle la ligne à la fin du parchemin
    parchment.appendChild(line);
};

// Envoie le message tapé : l'écrit sur le parchemin, puis l'envoie au serveur
function sendMessage() {
    writeLine(input.value, "sent");
    socket.send(input.value);
    input.value = "";
};


 // Au clic : écrit ton message sur le parchemin, puis l'envoie au serveur
button.onclick = sendMessage;

// Quand on appuie sur une touche dans le champ : si c'est Entrée, envoie le message
input.onkeydown = (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
};

// Quand un message arrive su serveur, affiche son texte dans le parchemin
socket.onmessage = (event) => {
  writeLine(event.data, "received");
};
