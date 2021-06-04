#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import os

import yaml

from common.generate_data import *


def is_release_environment():
    """
    True为正式环境
    :return:
    """
    is_release = True
    return is_release

class ServerConfig:
    def __init__(self):
        self.user_id = None
        self.user_token = None



    def get_http_server(self):
        """
        后台api地址
        :return:
        """
        if is_release_environment():
            return 'https://api.retail.melot.cn'
        else:
            return "http://10.4.24.93:10010"

    # def get_http_server(self):
    #
    #     return 'https://api.retail.melot.cn'

    def get_default_header(self, p, param, content_type):
        """
        header信息
        :param p:
        :return:
        """
        header = {
            "a": '1',
            "p": p,
            "c": '-1',
            "v": "0.0.1",
            "t": str(generate_current_time())
        }
        if self.user_id:
            header["loginUserId"] = self.user_id
        if self.user_token:
            header["loginToken"] = self.user_token
        if content_type == "application/json":
            headers = (header, "")
        elif content_type == "multipart/form-data":
            headers = generate_sv(header, "")
        else:
            headers = generate_sv(header, param)

        headers["Content-Type"] = content_type

        return headers

    def add_content_type_json(self):
        """
        :return: 增加content-type json类型,并返回
        """
        return "application/json"

    def add_content_type_form(self):
        """
        :return: 增加content-type表单类型,并返回
        """
        return "application/x-www-form-urlencoded"

    def get_data(self):
        with open(
                os.path.dirname(os.path.dirname(__file__)) + '/data/test_data.yml') as f:
            data = yaml.safe_load(f)
        return data
