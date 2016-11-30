#!/usr/bin/env python3.5

import unittest
import time
from macaca import WebDriver,WebElement

desired_caps = {
    'autoAcceptAlerts': True,
    'browserName': 'electron',
    'platformName': 'desktop'
}

server_url={
    'hostname':'127.0.0.1',
    'port':3456
}


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(onion):
        onion.driver=WebDriver(desired_caps,server_url)
        onion.driver.init()

    @classmethod
    def tearDownClass(onion):
        onion.driver.quit()

    def test_get_url(self):
        self.driver.get("http://www.baidu.com/")


    def test_search_item(self):
        self.driver.element_by_id('kw').send_keys('macaca')
        self.driver.element_by_id('su').click()
        time.sleep(3)
        html=self.driver.source
        self.assertTrue('macaca' in html)

if __name__=='__main__':
    unittest.main()
