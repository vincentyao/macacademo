#!/usr/bin/env python3.5
#-*- coding:utf8 -*-

from macaca import WebDriver, WebElement

# Configure the desired capabilities.
desired_caps = {
    'autoAcceptAlerts': True,
    'browserName': 'electron',
    'platformName': 'desktop'
}

driver = WebDriver(desired_caps)

# Start the WebDriver session
driver.init()

# Support fluent API
driver.set_window_size(1280, 800).get("http://www.baidu.com/")

# Get WebElement instance through element_by_* APIs.
web_element = driver.element_by_id("kw")
web_element.send_keys('macaca')
