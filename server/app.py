import json
from flask import Flask, request, send_from_directory, render_template
from flask_cors import cross_origin
from flask_talisman import Talisman, ALLOW_FROM

from computeImage import img_process
from computeImage import readBase64Img

import multiprocessing as mp

app = Flask(__name__)
talisman = Talisman(app, force_https=False, content_security_policy={})
mp.set_start_method('spawn')


@app.route('/', methods=['GET'])
def home():
    return send_from_directory('templates/home/public', 'index.html')


@app.route('/<path:path>')
def home_src(path):
    return send_from_directory('templates/home/public', path)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/API/upload', methods=['GET', 'POST'])
@talisman(frame_options=ALLOW_FROM, frame_options_allow_from='*')
@cross_origin()
def upload():
    if request.method == 'POST':
        req_json = request.json

        # print('json:', req_json["data"])

        if req_json["data"] == '' or req_json["data"] == None and req_json == None:
            return {
                "img": "fail"
            }

        img = readBase64Img(req_json["data"])

        if img != 'fail':
            q = mp.Queue()
            p = mp.Process(target=img_process, args=(img, q))
            p.start()
            ml_img = q.get()
            p.join()

            return {
                "img": ml_img
            }

        elif img == 'fail':
            return {
                "img": "fail"
            }

    elif request.method == 'GET':
        return {
            "error": "This is not a GET request!"
        }

    return {
        "error": "Something went wrong!"
    }
