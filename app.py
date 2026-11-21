from flask import Flask, jsonify

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"id": 3, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977},
]


@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify({"livros": livros})


if __name__ == "__main__":
    app.run(debug=True)