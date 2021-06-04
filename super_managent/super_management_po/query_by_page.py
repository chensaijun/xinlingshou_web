#! /usr/bin/python 3
# -*- coding:UTF8 -*
import requests

from common.base_api import BaseApi


class QuertByPage(BaseApi):
    def query_by_page(self, offset, pagesize):
        """
        品牌商分页查询
        :param offset:
        :param pagesize:
        :return:
        """
        url = self.header.get_http_server() + '/webapi/cloud/queryByPage'
        params = {
            "offset": offset,
            "pageSize": pagesize
        }
        content_type = self.header.add_content_type_form()
        headers = self.header.get_default_header("1", params, content_type)
        res = requests.get(url=url, params=params, headers=headers)
        self.log_debug(res)
        return res
