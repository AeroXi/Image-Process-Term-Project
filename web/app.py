from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from Morphology import dilate, erode, opening, close
from edge import get_edge
from filter import Filter
from thres import Thres
from fourier import Fourier
app = Flask(__name__)

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 形态学
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
        
# 边缘检测
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

# 直方图均衡化
@app.route('/equal/')
def equal():
    if request.args.get('function') is None:
        return render_template('equal.html')
    else:
        equal_in = cv2.imread('web/lena.jpg', 0)
        equal_out = cv2.equalizeHist(equal_in)
        cv2.imwrite('web/static/equal.jpg', equal_out)
        return send_file('static/equal.jpg', mimetype='image/jpeg')

# 图像平滑与锐化
@app.route('/filter/')
def filter():
    if request.args.get('function') is None:
        return render_template('filter.html')
    else:
        filter_in = cv2.imread('web/lena.jpg')
        function = request.args.get('function')
        kernel = int(request.args.get('kernel'))
        filter_out = Filter(filter_in, function, kernel)
        cv2.imwrite('web/static/filter.jpg', filter_out)
        return send_file('static/filter.jpg', mimetype='image/jpeg')

# 阈值化
@app.route('/thres/')
def thres():
    if request.args.get('value') is None:
        return render_template('thres.html')
    else:
        try:
            value = int(request.args.get('value'))
        except:
            value = None
        if value in range(-1, 256):
            thres_in = cv2.imread('web/lena.jpg', 0)
            thres_out = Thres(thres_in, value)
            cv2.imwrite('web/static/thres.jpg', thres_out)
            return send_file('static/thres.jpg', mimetype='image/jpeg')
        else:
            return '请输入0-255的阈值'

# 傅里叶变换
@app.route('/fourier/')
def fourier():
    if request.args.get('function') is None:
        return render_template('fourier.html')
    else:
        fourier_in = cv2.imread('web/lena.jpg', 0)
        fourier_out = Fourier(fourier_in)
        cv2.imwrite('web/static/fourier.jpg', fourier_out)
        return send_file('static/fourier.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port='80')