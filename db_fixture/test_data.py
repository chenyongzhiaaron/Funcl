import sys,time

sys.path.append('../db_fixture')

try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-100000))

# 定义当前时间
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))

# create data
datas_address = {
    'user_address': [
        {'user_id': 352, 'deliver_name': '初始化用户名', 'deliver_phone': 17727475174, 'deliver_address_country_id': 44,
         'deliver_address_province_id': 11,
         'deliver_address_city_id': 1101, 'deliver_address_district_id': 110101, "deliver_address": "初始化用户地址",
         "created_at": "2018-11-28 19:10:00", "updated_at": "2018-11-28 19:10:00",
         "deliver_address_country_name": "中国",
         "deliver_address_province_name": "北京市", "deliver_address_city_name": "市辖区",
         "deliver_address_district_name": "东城区"}
    ],

}


datas_fun_code = {
    'funcl_fun_codes': [
        {'fun_code': "MQZE1G57P3X72D9W", 'product_id': 92, 'active_time': past_time,
         'expiration_time': future_time, 'is_used': 0, 'code_type': "新品fun码",
         "created_at": current_time, "updated_at": current_time},   # 已激活，未到期，未使用
        {'fun_code': "WOINFO193841N009", 'product_id': 92, 'active_time': past_time,
         'expiration_time': future_time, 'is_used': 1, 'code_type': "新品fun码",
         "created_at": current_time, "updated_at": current_time},   # 已激活，未到期，已使用
        {'fun_code': "FWON9239J238J922", 'product_id': 92, 'active_time': past_time,
         'expiration_time': past_time, 'is_used': 0, 'code_type': "新品fun码",
         "created_at": past_time, "updated_at": past_time},         # 已激活，已到期，未使用
        {'fun_code': "92389NJ2H19DE183", 'product_id': 92, 'active_time': past_time,
         'expiration_time': past_time, 'is_used': 1, 'code_type': "新品fun码",
         "created_at": past_time, "updated_at": past_time},         # 已激活，已到期，已使用
        {'fun_code': "D12H872Y1010UJR0", 'product_id': 92, 'active_time': future_time,
         'expiration_time': future_time, 'is_used': 0, 'code_type': "新品fun码",
         "created_at": current_time, "updated_at": current_time},   # 未激活，未到期，未使用
        {'fun_code': "1EJ91HJR891H8191", 'product_id': 92, 'active_time': future_time,
         'expiration_time': future_time, 'is_used': 1, 'code_type': "新品fun码",
         "created_at": current_time, "updated_at": current_time},   # 未激活，未到期，已使用

    ],
}



# Inster table datas
def init_data():
    DB().init_data_address(datas_address)
    DB().init_data_fun_code(datas_fun_code)


if __name__ == '__main__':
    init_data()
