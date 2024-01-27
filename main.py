from flask import Flask, request, jsonify
from handlers.textHandler import process_metadata
from handlers.urlHandlers import analyze_url_meta

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

@app.route('/analyze-url', methods=['POST'])
def analyze_url_endpoint():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'No URL provided in the request'})

    try:
        result = analyze_url_meta(url)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': f"The provided string '{url}' doesn't look like a valid URL. Error: {str(e)}"})


if __name__ == '__main__':
    app.run()
