const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");
const personalitySelect = document.getElementById("personality");

input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendMessage();
    }
});

personalitySelect.addEventListener("change", function () {
    chatBox.innerHTML = "";
    input.value = "";
});

function sendMessage() {
    const message = input.value.trim();
    const personality = personalitySelect.value;
    if (!message) return;

    chatBox.innerHTML += `
        <div class="message-row user">
            <div class="bubble">${message}</div>
        </div>
    `;
    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ personality, message })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `
            <div class="message-row bot">
                <div class="bubble">${data.reply}</div>
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
