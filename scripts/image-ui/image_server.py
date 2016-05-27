import os
import shutil
import uuid

from flask import Flask, jsonify, send_file, request, url_for

from segment import open_image, save_image, segment_image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images/'
if os.path.exists(app.config['UPLOAD_FOLDER']):
    shutil.rmtree(app.config['UPLOAD_FOLDER'])
os.mkdir(app.config['UPLOAD_FOLDER'])

def _image_id():
	return str(uuid.uuid4())

def _image_url(image_id):
	return url_for('image', image_id=image_id)

def _image_path(image_id):
	return os.path.join(app.config['UPLOAD_FOLDER'], image_id + '.jpg')


@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	image_id = _image_id()
	file.save(_image_path(image_id))
	return jsonify(image_id=image_id, url=_image_url(image_id))

@app.route('/images/<string:image_id>')
def image(image_id):
	return send_file(_image_path(image_id))

@app.route('/segment/<string:image_id>')
def segment(image_id):
	image = open_image(_image_path(image_id))
	segmented = segment_image(image)
	image_id = _image_id()
	save_image(_image_path(image_id), segmented)
	return jsonify(image_id=image_id, url=_image_url(image_id))


if __name__=='__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)
	app.logger.info("Server shuting down")