import sys,os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

sys.path.append('./interface/')
sys.path.append('./db_fixture')
sys.path.append('./Global_bse')

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = 'F:\/auto\qsjInterface\interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

if __name__ == "__main__":
    # test_data.init_data()  # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "F:\/auto\qsjInterface\/report/" + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='QSJ API Test Report',
                            description='Implementation Example with: QSJ_API_Test_Report')
    runner.run(discover)
    fp.close()
