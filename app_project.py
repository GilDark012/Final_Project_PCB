from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    return render_template('index.html')

if __name__ == '__main__':
    app.run( port=5000, debug=True)