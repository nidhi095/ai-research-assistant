import logging
from flask import Flask, request, jsonify

# Setup logging
logging.basicConfig(filename='logs/app.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "no file part"}), 400
        
        f = request.files['file']
        text = f.read().decode('utf-8')
        words = text.split()

        # Log success
        logging.info(f"Uploaded {f.filename} size={len(text)}")

        return jsonify({"filename": f.filename, "word_count": len(words)})
    
    except Exception as e:
        logging.exception("Upload failed")
        return jsonify({"error": "internal error"}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
