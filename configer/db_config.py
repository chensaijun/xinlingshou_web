#! /usr/bin/python 3
# -*- coding:UTF8 -*-
def get_redis_config():
    host = '10.4.7.171'
    port = '6379'
    db = ''
    password = 'redis#1234A'
    return host, port, db, password


def get_pg_user_config():
    database = 'syds_user'
    user = 'syds_user_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_item_config():
    database = 'syds_item'
    user = 'syds_item_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_trade_config():
    database = 'syds_trade'
    user = 'syds_trade_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_shop_config():
    database = 'syds_shop'
    user = 'syds_shop_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_common_config():
    database = 'syds_common'
    user = 'syds_common_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_pay_config():
    database = 'syds_pay'
    user = 'syds_pay_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_wuliu_config():
    database = 'syds_wuliu'
    user = 'syds_wuliu_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port


def get_pg_clear_config():
    database = 'syds_clear'
    user = 'syds_clear_dev'
    password = 'syds123'
    host = '10.4.24.13'
    port = '5432'
    return database, user, password, host, port
