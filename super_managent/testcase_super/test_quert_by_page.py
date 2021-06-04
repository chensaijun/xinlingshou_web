#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import os

import allure
import pytest
import yaml

from configer.server_config import ServerConfig
from super_managent.super_management_po.query_by_page import QuertByPage


@allure.feature('品牌商分页查询')
@allure.story('品牌商分页查询')
@allure.title('品牌商分页查询')
@allure.description('品牌商分页查询')
class TestQuertByPage:
    def setup(self):
        self.list = QuertByPage()
        self.get_data = ServerConfig()

    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.develop
    def test_quert_by_page(self):
        data = self.get_data.get_data()
        offset = data['page']['offset']
        pageSize = data['page']['pageSize']
        r = self.list.query_by_page(offset, pageSize)
        assert r.json()["success"] == True
