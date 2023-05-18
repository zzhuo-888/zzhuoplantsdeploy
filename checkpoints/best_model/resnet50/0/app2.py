from flask import Flask 
app = Flask(__name__)
 
@app.route('/')
def predict():
	return "hello world!  It is flask!"
	
if __name__ == '__main__':
    app.run()