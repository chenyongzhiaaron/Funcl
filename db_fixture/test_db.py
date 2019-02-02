# coding=utf-8

import pymysql.cursors
import os
import configparser as cparser
import pymysql.cursors

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


class T_DB():
    #   通过数据库获取用户最新的一条验证码
    # def t_db(self):
    #     # 连接MySQL数据库
    #     connection = pymysql.connect(host=host,
    #                                  port=int(port),
    #                                  user=user,
    #                                  password=password,
    #                                  db=db,
    #                                  charset='utf8mb4',
    #                                  cursorclass=pymysql.cursors.DictCursor)  # 测试数据库
    #
    #     # connection = pymysql.connect(
    #     #     host='cb-test.c6g84obm21ye.us-west-1.rds.amazonaws.com',
    #     #     port=3306,
    #     #     user='crazybb_test',
    #     #     password='crazybb_test',
    #     #     db='crazybb_test',
    #     #     charset='utf8mb4',
    #     #     cursorclass=pymysql.cursors.DictCursor
    #     # )                                                                         # 测试服数据库
    #     # 通过cursor创建游标
    #     cursor = connection.cursor()
    #     # 创建sql 语句，并执行
    #     sqlCaptcha = "select content from laravel_sms order by updated_at desc limit 1"  # 获取最新一条验证码记录
    #     cursor.execute(sqlCaptcha)
    #     # 查询单条数据
    #     # result = cursor.fetchone()
    #     # 查询多条数据
    #     result = cursor.fetchall()
    #     # 循环打印数据结果
    #     #         for date in result:
    #     #             print(date)
    #
    #     # 切割获取数据验证码部分
    #     for item in result:
    #         temp = item["content"].split("，请于5分钟")[0].split("【signature】您的验证码是")[1]
    #         # print(temp)
    #     # 提交SQL
    #     # connection.commit()
    #     # 关闭数据连接
    #     connection.close()
    #     return temp

    #   ----------------------------------------------------------我是分割线--------------------------------------------

    #   通过数据库获取用户最新的一条验证码
    def t_db2(self):
        # 连接MySQL数据库
        connection = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)  # 田科本地测试数据库
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句，并执行
        sqlCaptcha = "select smscode from sinaif_easy.t_app_smsinfo where mobile = 18570000000 order by sendtime desc limit 1"  # 获取最新一条用户验证码
        cursor.execute(sqlCaptcha)
        # 查询单条数据 并将结果返回给 result
        result = cursor.fetchone()
        # 查询多条数据 并将结果返回给 result
        # result = cursor.fetchall()
        smscode = result['smscode']
        # 关闭数据连接
        connection.close()
        return smscode

test = T_DB()
print(test.t_db2())
smscode = test.t_db2()
# print("api/user/address/" + str(address_id))
print(smscode)