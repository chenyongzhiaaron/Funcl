import sys

sys.path.append('../db_fixture')

try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    'user_address': [
        {'user_id': 352, 'deliver_name': '测试工作者', 'deliver_phone': 17727475174, 'deliver_address_country_id': 44,
         'deliver_address_province_id': 11,
         'deliver_address_city_id': 1101, 'deliver_address_district_id': 110101, "deliver_address": "测试办公室",
         "created_at": "2018-11-28 19:10:00", "updated_at": "2018-11-28 19:10:00",
         "deliver_address_country_name": "中国",
         "deliver_address_province_name": "北京市", "deliver_address_city_name": "市辖区",
         "deliver_address_district_name": "东城区"}
    ],
    # 'funcl_fun_codes': [
    #     {'fun_code': "F29H3912H89FR2H8", 'product_id': 90, 'active_time': "2018-12-17 13:55:13", 'expiration_time': '2018-12-31 13:55:15', 'is_used': 0, 'code_type': "新品fun码", "created_at": "2018-12-18 13:55:21", "updated_at": "2018-12-18 07:10:21"},
    #     {'fun_code': "F29H3912H89FR2H8", 'product_id': 90, 'active_time': "2018-12-17 13:55:13", 'expiration_time': '2018-12-31 13:55:15', 'is_used': 0, 'code_type': "新品fun码", "created_at": "2018-12-18 13:55:21", "updated_at": "2018-12-18 07:10:21"},
    #
    # ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
