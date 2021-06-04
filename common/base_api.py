#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import json
import os

import pytest
import yaml

from configer.log_config import Log
from configer.server_config import *


class BaseApi():
    def __init__(self):
        self.header = ServerConfig()
        self.log = Log()
        with open(
                os.path.dirname(os.path.dirname(__file__)) + '/data/login_data.yml') as f:
            data = yaml.safe_load(f)
            user_id = data['header_param']['user_id']
            user_token = data['header_param']['user_token']
        self.header.user_id = user_id
        self.header.user_token = user_token


    def log_debug(self, param):
        res_json = json.dumps(param.json(), indent=2, ensure_ascii=False)
        return self.log.debug(res_json)
