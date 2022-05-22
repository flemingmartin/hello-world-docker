from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	print("Connection OK")
	return "AAASHHEEEEEEE"


if __name__ == "__main__":
	print("Flsk server on!")
	app.run(debug=True, host='0.0.0.0')
