import os
from flask import send_file, jsonify

def handle_image_request(image_path):
    image_full_path = os.path.join("images/", image_path)

    if os.path.exists(image_full_path):
        return send_file(image_full_path), 200
    else:
        return jsonify({'error': f'Image {image_path} not found'}), 404
