from flask import Flask, render_template, request, jsonify
import algorithms.huffman as huffman
import algorithms.arithmetic as arithmetic
import algorithms.rle as rle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    text = request.form['text']
    algorithm = request.form['algorithm']

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        if algorithm == 'huffman':
            compressed, tree = huffman.compress(text)
            response = {"compressed": compressed, "tree": tree}
        elif algorithm == 'arithmetic':
            compressed = arithmetic.compress(text)
            response = {"compressed": compressed}
        elif algorithm == 'rle':
            compressed = rle.compress(text)
            response = {"compressed": compressed}
        else:
            return jsonify({"error": "Invalid algorithm selected"}), 400

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

