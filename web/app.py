from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from Morphology import dilate, erode, opening, close
from edge import get_edge
app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/morph/')
def morph():
    if request.args.get('function') is None:
        return render_template('morph.html')
    else:
        morph_in = cv2.imread('web/lena.jpg', 0)
        function = request.args.get('function')
        kernel = int(request.args.get('kernel'))
        if function == 'open':
            morph_out = opening(morph_in, kernel)
        elif function == 'close':
            morph_out = close(morph_in, kernel)
        elif function == 'dilate':
            morph_out = dilate(morph_in, kernel)
        elif function == 'erode':
            morph_out = erode(morph_in, kernel)
        cv2.imwrite('web/static/morph.jpg', morph_out)
        return send_file('static/morph.jpg', mimetype='image/jpeg')
        
@app.route('/edge/')
def edge():
    if request.args.get('function') is None:
        return render_template('edge.html')
    else:
        edge_in = cv2.imread('web/lena.jpg', 0)
        function = request.args.get('function')
        edge_out = get_edge(edge_in, function)
        cv2.imwrite('web/static/edge.jpg', edge_out)
        return send_file('static/edge.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')