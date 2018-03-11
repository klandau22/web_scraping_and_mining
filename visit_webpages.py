#! usr/bin/python3

'''
This script will be used to automatically visit a particular webpage at a certain time everyday with the specified account you desire.
'''

# Kevin Landau, MS
# 11/1/2017

#nil

# 12/21/2017 - resumed this project while on winter break from med school...

# download and import selenium package.

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
mydriver = webdriver.Firefox()

# Let's use stack overflow as an example url.
mydriver.get("https://stackoverflow.com/")
wait = ui.WebDriverWait(mydriver, 10)
wait.until(page_is_loaded)

# Got error: selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH., so I downloaded the latest geckodriver from GitHub

# Still need to set correct variable PATHs b/w windows system and the Unix (Ubuntu) shell


# Downloaded Git to local machine on 1/2/18 and initialized repository.


