from flask import Flask, request, jsonify, render_template
from chatbot import chat

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# 👉 HOME PAGE ROUTE (YE MISS THA)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.json
    personality = data.get("personality")
    message = data.get("message")

    if not personality or not message:
        return jsonify({"reply": "Invalid request"}), 400

    reply = chat(personality, message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
