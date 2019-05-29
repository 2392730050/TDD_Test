from selenium import  webdriver
import time
import  unittest
# driver = webdriver.Chrome()
# driver.get("http://118.25.216.133:8000/")
# time.sleep(3)
# print(driver.title)
# assert 'EasyTest-自动化测试平台' in driver.title
#
# driver.quit()

class test(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()
    def test_1(self):
        self.driver.get("http://118.25.216.133:8000/")
        self.assertIn("EasyTest-自动化测试平台",self.driver.title)
        #不管是否成功都抛出异常
        #self.fail("Finish the test")
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore')
