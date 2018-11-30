import sys

sys.path.append('../db_fixture')

try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    'user_address': [
        {'user_id': 349, 'deliver_name': '测试工作者', 'deliver_phone': 13800138000, 'deliver_address_country_id': 44,
         'deliver_address_province_id': 11,
         'deliver_address_city_id': 1101, 'deliver_address_district_id': 110101, "deliver_address": "测试办公室",
         "created_at": "2018-11-28 19:10:00", "updated_at": "2018-11-28 19:10:00",
         "deliver_address_country_name": "中国",
         "deliver_address_province_name": "北京市", "deliver_address_city_name": "市辖区",
         "deliver_address_district_name": "东城区"}
    ],
    # 'sign_guest': [
    #     {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1},
    #     {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'event_id': 1},
    #     {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'event_id': 5},
    # ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
