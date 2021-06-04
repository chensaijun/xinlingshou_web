# #! /usr/bin/python 3
# # -*- coding:UTF8 -*-
# import requests
#
# from common.base_api import BaseApi
# from configer.log_config import Log
#
# from configer.server_config import *
#
#
# class LoginSuper(BaseApi):
#     log = Log()
#
#     def login_super(self, user_name, password, p, code):
#         """
#         超管后台登录
#         :param user_name:
#         :param password:
#         :param p: SUPER_ADMIN(1, "超管后台"),
#                   BRAND_ADMIN(2, "品牌商后台"),
#                   SHOP_ADMIN_WEB(3, "分店后台web"),
#                   SHOP_ADMIN_APP_IOS(4, "分店后台ios"),
#                   SHOP_ADMIN_APP_ANDRIOD(5, "分店后台安卓"),
#                   CUSTOMER_XCX(6, "客户端小程序")
#         :param code:
#         :return:
#         """
#         url = self.config.get_http_server() + '/webapi/login/superadmin'
#         params = {
#             "username": user_name,
#             "password": generate_psw(password),
#             "p": p,
#             "code": code
#         }
#         content_type = self.config.add_content_type_form()
#         headers = self.config.get_default_header("1", params, content_type)
#         res = requests.get(url=url, params=params, headers=headers)
#         self.log_debug(res)
#         is_true = res.json()['success']
#
#         if is_true is True:
#             user_id = res.json()['object']['userVo']['id']
#             self.log.info('user_id' + str(user_id))
#             user_token = res.json()['object']['token']
#             self.log.info('user_token' + user_token)
#             return str(user_id),user_token
#         else:
#             self.log.error(res.json())
#             return None,None
#
#
