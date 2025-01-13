# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:59:21 2025

@author: ziedk
"""

import os
os.chdir('C:/Users/ziedk/OneDrive/Bureau/Data Science Projects/Medicine Search')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://base-donnees-publique.medicaments.gouv.fr/liste-medicaments-a.php')

x = driver.find_elements(By.CLASS_NAME,"ResultRowDeno")


x[3].find_element(By.TAG_NAME,'a').get_attribute('href')


def get_links_one_page():
    """
    This function parses through a single page for example with letter A and extracts all the links leading to the information page of a drug

    return -> list of links
    """
    rows_in_page = driver.find_elements(By.CLASS_NAME,"ResultRowDeno")
    links_in_page = [i.find_element(By.TAG_NAME,'a').get_attribute('href') for i in rows_in_page]
    return links_in_page

def get_links_all_pages():
    """
    Enter a letter to get a new page and then extract the links of all the drugs starting with that letter

    return -> dictionary in the format {'A':['link1','link2'...],'B':...}
    -------
    """
    
    


character

x = driver.find_element(By.NAME,'txtCaracteres')
x.send_keys('B')
x.clear()
y = driver.find_element(By.NAME,'btnMedic')
y.click()