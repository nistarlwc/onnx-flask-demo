#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import multiprocessing
multiprocessing.set_start_method('spawn')

from flask import Flask, request, jsonify
import os,time,cv2,json, base64, traceback
import numpy as np
import onnxruntime as rt
from inference import runsess

app = Flask(__name__)

def bytes2cv(data):
    nparr = np.fromstring(data, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img_decode

def predict_multi_label(sess, image):
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name

    new_image = []
    if len(image.shape) < 3:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = cv2.resize(image, (768, 768), interpolation=cv2.INTER_LINEAR)
    new_image.append(image)
    im_in = new_image
    im_in = np.float32(im_in) / 255.0

    prediction = sess.run([label_name], {input_name: np.array(im_in, dtype=np.float32)})[0]
    return prediction

@app.route('/algorithm/api', methods=['POST'])
def parser():
    code = 0
    try:
        start_time = time.time()
        data = request.get_data()
        if isinstance(data, bytes):
            data = str(data, encoding="utf-8")
        data = json.loads(data, strict=False)

        image_base64 = data["image_base64"]
        if image_base64 != 'None':
            binary_data = base64.b64decode(image_base64)
            cv_image = bytes2cv(binary_data)
        else:
            cv_image = cv2.imread(data["image_path"], 0)

        print("session id: ", id(runsess))
        prediction = predict_multi_label(runsess, cv_image)

        end_time = time.time()
        total_time = (end_time - start_time) * 1000
        print("THE SERVICE FINISHED, RUN TIME IS:  %s\n\n" % (total_time))
        code = 1
        response_data = {"flag": 1}
    except:
        # traceback.print_exc()
        error_string = traceback.format_exc()
        print(" !!!! HTTP SERVICE CALL FAILED !!!!")
        print('Http service error info: %s' % error_string)
        code = 101
        response_data = {}

    return jsonify({
        'code': code,
        'data': response_data
    })

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=23456, processes=True)
