import configparser
import os
class TestReadConfig(object):
    def get_value(self):
        root_dir=os.path.dirname(os.path.abspath('.'))#获取根目录的相对路径,/Users/Tiernan/PycharmProjects
        print(root_dir)
        config=configparser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/python_learn/config.ini'
        config.read(file_path)
        browser=config.get('browserType','browserName')
        url=config.get('testUrl','url')
        return (browser,url)#返回元祖
test=TestReadConfig()
print(test.get_value())
