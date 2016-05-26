import os

from flask import Flask, jsonify, send_file, request, url_for, send_from_directory
from werkzeug import secure_filename

import numpy as np
from PIL import Image

from segment import segment, save_image, open_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images/'


@app.route('/segment', methods=['POST'])
def _segment():
	file = request.files['file']
	filename = secure_filename(file.filename)
	image = open_image(file)
	segmented = segment(image)
	output_name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	save_image(output_name, segmented)
	return jsonify(url=url_for('_image', filename=filename))

@app.route('/images/<filename>')
def _image(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__=='__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)
	app.logger.info("Server shuting down")