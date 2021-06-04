#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import allure
import pytest


@pytest.mark.smoke
@pytest.mark.release
@allure.feature('帐号登录用例')
@allure.story('帐号登录用')
@allure.title('帐号登录用例')
@allure.description('帐号登录用例')
def test_login(login_super):
    user_id, user_token = login_super
    assert user_id is not None and user_token is not None
    pass
