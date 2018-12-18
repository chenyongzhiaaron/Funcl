import pymysql.cursors


# -*- coding: UTF-8 -*-

class T_DB():
    #   通过数据库获取用户最新的一条验证码
    def t_db(self):
        # 连接MySQL数据库
        connection = pymysql.connect(host='192.168.1.45',
                                     port=3306,
                                     user='remote',
                                     password='123456',
                                     db='crazybaby',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)  # 田科本地测试数据库

        # connection = pymysql.connect(
        #     host='cb-test.c6g84obm21ye.us-west-1.rds.amazonaws.com',
        #     port=3306,
        #     user='crazybb_test',
        #     password='crazybb_test',
        #     db='crazybb_test',
        #     charset='utf8mb4',
        #     cursorclass=pymysql.cursors.DictCursor
        # )                                                                         # 测试服数据库
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句，并执行
        sqlCaptcha = "select content from laravel_sms order by updated_at desc limit 1"  # 获取最新一条验证码记录
        cursor.execute(sqlCaptcha)
        # 查询单条数据
        # result = cursor.fetchone()
        # 查询多条数据
        result = cursor.fetchall()
        # 循环打印数据结果
        #         for date in result:
        #             print(date)

        # 切割获取数据验证码部分
        for item in result:
            temp = item["content"].split("，请于5分钟")[0].split("【signature】您的验证码是")[1]
            # print(temp)
        # 提交SQL
        # connection.commit()
        # 关闭数据连接
        connection.close()
        return temp

    #   ----------------------------------------------------------我是分割线--------------------------------------------

    #   通过数据库获取用户最新的一条地址
    def t_db2(self):
        # 连接MySQL数据库
        connection = pymysql.connect(host='192.168.1.45',
                                     port=3306,
                                     user='remote',
                                     password='123456',
                                     db='crazybaby',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)  # 田科本地测试数据库
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句，并执行
        sqlCaptcha = "select id from user_address where user_id = 352 order by id desc limit 1"  # 获取最新一条用户地址记录
        cursor.execute(sqlCaptcha)
        # 查询单条数据 并将结果返回给 result
        result = cursor.fetchone()
        # 查询多条数据 并将结果返回给 result
        # result = cursor.fetchall()
        address_id = result['id']
        # 关闭数据连接
        connection.close()
        return address_id

# test = T_DB()
# # print(test.t_db())
# address_id = test.t_db2()
# print("api/user/address/" + str(address_id))
