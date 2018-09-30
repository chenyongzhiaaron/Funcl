import sys
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

sys.path.append('./Administrator')
sys.path.append('./db_fixture')

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Funcl_API_Test_Report',
                            description='Implementation Example with: Funcl_API_Test_Report')
    runner.run(discover)
    fp.close()
