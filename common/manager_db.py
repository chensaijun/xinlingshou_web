#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import psycopg2 as psycopg2
from redis import StrictRedis

from configer.db_config import *
from configer.log_config import Log

log = Log()


def execute_pg_db(sql, type):
    """
    连接数据库
    :param sql:
    :param type:
    :return:
    """

    rows = None
    if sql is None:
        return rows
    if type == 'user':
        database, user, password, host, port = get_pg_user_config()
    elif type == 'item':
        database, user, password, host, port = get_pg_item_config()
    elif type == 'trade':
        database, user, password, host, port = get_pg_trade_config()
    elif type == 'shop':
        database, user, password, host, port = get_pg_shop_config()
    elif type == 'common':
        database, user, password, host, port = get_pg_common_config()
    elif type == 'pay':
        database, user, password, host, port = get_pg_pay_config()
    elif type == 'wuliu':
        database, user, password, host, port = get_pg_wuliu_config()
    elif type == 'clear':
        database, user, password, host, port = get_pg_clear_config()
    else:
        print("需配置新的数据库")
    try:
        # 连接数据库
        connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.close()
    except Exception as e:
        log.error(e)
    return rows


def execute_redis_db(key):
    """
    连接redis
    :param key:
    :return:
    """
    value = None
    if key is None:
        return value
    try:
        host, port, db, password = get_redis_config()
        redis_pool = StrictRedis(host=host, port=port, db=db, password=password)
        log.error(redis_pool.keys())
        value = redis_pool.get(key)
    except Exception as e:
        log.error(e)
    return value
