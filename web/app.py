from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/morph/')
def morph():
    return render_template('morph.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')