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
import time 

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
    Parses through all the pages for each letter and extract all the links in each page

    return -> dictionary in the format {'A':['link1','link2'...],'B':...}
    -------
    """
    links_per_page = dict()
    
    letter_page_elements = driver.find_elements(By.CLASS_NAME,'lienalphabet')
    character = [chr(i) for i in range(ord('A'), ord('B') + 1)]
    for i in range(1,3):

        driver.find_elements(By.CLASS_NAME,'lienalphabet')[i].click()
        links_current_page = get_links_one_page()
        time.sleep(3)
        print(links_current_page)
        links_per_page[character[i]] = links_current_page
    return links_per_page
        
          
        
all_drugs_links = get_links_all_pages()


