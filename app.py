from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error":"no file part"}), 400
    f = request.files['file']
    text = f.read().decode('utf-8')
    words = text.split()
    return jsonify({"filename": f.filename, "word_count": len(words)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
