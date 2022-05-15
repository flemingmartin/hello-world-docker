from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	print("Connection OK")
	return "Insta updateado (Puto el que lee)"


if __name__ == "__main__":
	print("Flsk server on!")
	app.run(debug=True, host='0.0.0.0')
