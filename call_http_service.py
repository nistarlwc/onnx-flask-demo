# coding: utf-8
import os
import requests
import time
import base64, json
import cv2
import random


def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            if cur_path.endswith('.bmp') or cur_path.endswith('.jpg') or cur_path.endswith('.png'):
                all_files.append(cur_path)

    return all_files

if __name__ == '__main__':
    print('bingo...')
    image_file_path = r"image"

    # 定义IP地址和端口号
    test_host, test_port = "127.0.0.1", "23456"
    request_url = "http://{}:{}/algorithm/api".format(test_host, test_port)
    use_base64 = 1
    image_name_list = os.listdir(image_file_path)
    for n in range(10):
        image_name_list += image_name_list

    allTime = 0
    for id, image_name in enumerate(image_name_list):
        image_file_name = os.path.join(image_file_path, image_name)
        # image_file_name = image_name
        print(image_file_name)
        start2 = time.time()
        if use_base64:
            start2 = time.time()
            f = open(image_file_name, 'rb')
            image_data = f.read()
            f.close()

            # 定义要发送的数据包的数据结构
            req_json = {
                "image_name": image_name,  # image_name: panelID_ZM_L_S_0.bmp,
                "image_path": image_file_name,
                "image_base64": base64.b64encode(image_data).decode(),
            }
        else:
            req_json = {
                "image_name": image_name,  # image_name: panelID_ZM_L_S_0.bmp,
                "image_path": image_file_name,
                "image_base64": 'None',

            }

        response_return = requests.post(request_url, json=req_json).json()["data"]
        # print(response_return['defect_rslt_list'])
        print(response_return['flag'])
        end2 = time.time()
        total2 = (end2 - start2) * 1000
        allTime += total2
        print("______run time is: ", total2)
    print("total time is: ", allTime)

