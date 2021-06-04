#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
if path not in sys.path:
    sys.path.append(path)

import pytest
import requests
import json

from configer.log_config import Log

from configer.server_config import *
from super_managent.super_management_po.get_image_code import GetImageCode

log = Log()
header = ServerConfig()


@pytest.fixture(scope='session', autouse=True)
def cmdoption(request):
    myenv = request.config.getoption("--login_super", default='release')

    if myenv == 'test':
        datapath = '/data/test_data.yml'
    elif myenv == 'release':
        datapath = "/data/release_data.yml"

    with open(path + datapath) as f:
        datas = yaml.safe_load(f)
    print(datas)
    return myenv, datas


@pytest.fixture(scope='session', autouse=True)
def login_super(cmdoption):
    """
    超管后台登录
    :param user_name:
    :param password:
    :param p: SUPER_ADMIN(1, "超管后台"),
              BRAND_ADMIN(2, "品牌商后台"),
              SHOP_ADMIN_WEB(3, "分店后台web"),
              SHOP_ADMIN_APP_IOS(4, "分店后台ios"),
              SHOP_ADMIN_APP_ANDRIOD(5, "分店后台安卓"),
              CUSTOMER_XCX(6, "客户端小程序")
    :param code:
    :return:
    """
    login_super, datas = cmdoption
    user_name = datas['login_super']['user_name']
    password = datas['login_super']['password']
    p = datas['login_super']['p']

    get_code = GetImageCode().get_image_code(p)
    code = get_code.json()['object']['content']

    url = header.get_http_server() + '/webapi/login/superadmin'
    params = {
        "username": user_name,
        "password": generate_psw(password),
        "p": p,
        "code": code
    }
    content_type = header.add_content_type_form()
    headers = header.get_default_header(p, params, content_type)
    res = requests.get(url=url, params=params, headers=headers)
    log.debug(json.dumps(res.json(), indent=2, ensure_ascii=False))
    is_true = res.json()['success']

    if is_true is True:
        user_id = res.json()['object']['userVo']['id']
        log.info('user_id:' + str(user_id))
        user_token = res.json()['object']['token']
        log.info('user_token:' + user_token)
        param = {
            'header_param': {
                'user_id': str(user_id),
                'user_token': user_token
            }

        }
        with open(path + '/data/login_data.yml', 'w', encoding='utf-8') as f:
            yaml.dump(param, f)
        return str(user_id), user_token
    else:
        log.error(res.json())
        return None, None
