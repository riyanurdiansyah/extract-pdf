from flask import Flask, request, jsonify
import json
from service import extract
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/api/extract', methods=['GET'])
def get_fruits():
    data = extract();
    return jsonify(data)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    if file and allowed_file(file.filename):
        # Read the PDF file and extract text
        pdf_text = extract_text_from_pdf(file)
        return jsonify({'text': pdf_text})
    else:
        return jsonify({'error': 'Invalid file format. Only PDF files are allowed.'})

def allowed_file(filename):
    # Define the allowed file extensions
    allowed_extensions = {'pdf'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file);
    text = ""

    for index, pdf_page in enumerate(pdf_reader.pages):
        text += pdf_page.extract_text()

    return text

if __name__ == '__main__':
    app.run(debug=True)

