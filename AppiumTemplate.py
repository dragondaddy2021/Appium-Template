'''
此範本使用Python語言，使用Appium框架來進行APP自動化測試。
setUp()函式用於初始化Appium設定，
test_login()和test_logout()函式則用於執行登入和登出測試。
最後，tearDown()函式用於結束測試。

此範本只是一個基本的程式樣板，
實際測試會根據不同的APP和測試需求進行修改。
'''


import unittest
from appium import webdriver

class AppTest(unittest.TestCase):

    def setUp(self):
        # 初始化Appium設定
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '14.0'
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['app'] = '/path/to/app'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_login(self):
        # 登入測試
        self.driver.find_element_by_id('username').send_keys('testuser')
        self.driver.find_element_by_id('password').send_keys('testpassword')
        self.driver.find_element_by_id('login_button').click()
        self.assertEqual(self.driver.current_activity, 'MainActivity')

    def test_logout(self):
        # 登出測試
        self.driver.find_element_by_id('logout_button').click()
        self.assertEqual(self.driver.current_activity, 'LoginActivity')

    def tearDown(self):
        # 結束測試
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
