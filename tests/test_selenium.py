from __future__ import print_function, division
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os
from subprocess import check_output


class TestMain(unittest.TestCase):
    def test_main(self):
        os.environ["FLASK_APP"] = "demo.demo"
        os.environ["FLASK_DEBUG"] = "1"
        os.system("flask run --host 0.0.0.0 --port 5000 &")
        time.sleep(5)
 
        url = 'http://127.0.0.1:5000/'
        
        driver = webdriver.PhantomJS()
        driver.get(url)
        assert "Python Test site" == driver.title
        #print(driver)   # selenium.webdriver.chrome.webdriver.WebDriver
        links = driver.find_elements_by_tag_name("a")
        #print(links)
        assert len(links) == 6
        assert links[0].get_attribute('href') == url
        assert links[1].get_attribute('href') == url + 'echo'
        assert links[2].get_attribute('href') == url + 'login'
        assert links[3].get_attribute('href') == url + 'secure-login'
        assert links[4].get_attribute('href') == url + 'account'
        assert links[5].get_attribute('href') == url + 'other'
        #time.sleep(20)
        
        link = driver.find_element_by_link_text('Echo')
        #print(link)
        link.click()
        assert 'Echo' == driver.title
        assert '<div id="get_response"></div>' in driver.page_source
        assert '<div id="post_response"></div>' in driver.page_source
        assert '<div id="ajax_get_response"></div>' in driver.page_source
        assert '<div id="ajax_post_response"></div>' in driver.page_source
        
        #print(driver.page_source)
        #driver.find_element_by_id('getter')
        #print("Echo page")
        elem = driver.find_element_by_id('txt')
        #print(elem)
        elem.send_keys("hello world")
        elem.send_keys(Keys.RETURN)
        #print(driver.page_source)
        time.sleep(2)
        assert '<div id="get_response">You said: hello world</div>' in driver.page_source
        
        driver.back()
        assert '<div id="get_response"></div>' in driver.page_source
        
        #elem = driver.find_element_by_id('msg')
        
        driver.close()

        #pid = check_output(["ps", 'axuw'])
        print(pid)
        #os.kill(pid)
# vim: expandtab

