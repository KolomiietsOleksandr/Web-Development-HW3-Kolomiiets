from flask import Flask, request, jsonify
from handlers.textHandler import process_metadata

app = Flask(__name__)

@app.route('/')
def initial():
    return 'Main page'

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' in request.files:
        file = request.files['file']
        file_contents = file.read().decode('utf-8')
    elif 'string' in request.form:
        file_contents = request.form['string']
        print("string")
    else:
        return 'No file or string provided in the request'

    search_string = request.form.get('search_string', '')

    if search_string:
        metadata = process_metadata(file_contents, search_string)
        return jsonify(metadata)
    else:
        return 'No search_string provided in the request'

if __name__ == '__main__':
    app.run()
