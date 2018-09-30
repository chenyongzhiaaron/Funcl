import pymysql.cursors


class T_DB():
    def t_db(self):
        # 连接MySQL数据库
        # connection = pymysql.connect(host='192.168.1.45', port=3306, user='aaron', password='123456', db='crazybaby',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)         # 本地测试数据库

        connection = pymysql.connect(
            host='cb-test.c6g84obm21ye.us-west-1.rds.amazonaws.com',
            port=3306,
            user='crazybb_test',
            password='crazybb_test',
            db='crazybb_test',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        # 通过cursor创建游标
        cursor = connection.cursor()

        # 创建sql 语句，并执行
        sql = "select content from laravel_sms order by updated_at desc limit 1"
        cursor.execute(sql)

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
            # print(temp[1])

            # 提交SQL
            # connection.commit()
            return temp
