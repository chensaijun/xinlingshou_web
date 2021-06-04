#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import json

import requests
from common.base_api import BaseApi, ServerConfig
from configer.log_config import Log


class GetImageCode:
    header = ServerConfig()
    log = Log()
    def get_image_code(self, p):
        """
        获取验证码
        :param p:
        :return:
        """
        url = self.header.get_http_server() + '/webapi/image/code'
        params = {
            "p": p,
        }
        content_type = self.header.add_content_type_form()
        headers = self.header.get_default_header("1", params, content_type)
        res = requests.get(url=url, params=params, headers=headers)
        self.log.debug(json.dumps(res.json(), indent=2, ensure_ascii=False))
        return res


if __name__ == '__main__':
    a = GetImageCode()
    r = a.get_image_code(1)
