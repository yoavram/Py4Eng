from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Test this server by going to <a href="http://127.0.0.1:5223/len/python">/len/python</a>'

@app.route('/len/<word>')
def wordlen(word):
    return str(len(word))

if __name__ == '__main__':
	print("Test this server by going to http://127.0.0.1:5223/len/python")
	app.run(port=5223, debug=True)