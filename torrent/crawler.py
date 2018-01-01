#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
  from bs4 import BeautifulSoup
except ImportError:
  print("Please install.")
  print("pip install bs4.")
  exit(255)
 
try:
  from selenium import webdriver
except ImportError:
  print("Please install.")
  print("pip install selenium.")
  exit(255)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import sys
import argparse

# Use in a cloud environment where the browser can not be output.
"""
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()
"""

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--chromedriver',
    type=str,
    default='/usr/local/bin/chromedriver',
    help='Location of chromedriver.')
  parser.add_argument(
    '--site',
    type=str,
    default='https://example.kr',
    help='Your website address.')
  parser.add_argument(
    '--id',
    type=str,
    default='foo',
    help='Your site ID.')
  parser.add_argument(
    '--passwd',
    type=str,
    default='bar',
    help='Your site password.')

  FLAGS, unparsed = parser.parse_known_args()

  browser = webdriver.Chrome(FLAGS.chromedriver)
  browser.implicitly_wait(3)

  browser.get(FLAGS.site)
  delay = 10 # seconds
  try:
    # FIXME. 'mb_id' is a special element of the site.
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'mb_id')))
    print("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")
    exit(255)

  browser.find_element_by_name('mb_id').send_keys(FLAGS.id)
  browser.find_element_by_name('mb_password').send_keys(FLAGS.passwd)
  browser.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()
  browser.find_element_by_xpath('//*[@id="talk_submit"]').click()
  browser.quit()
  print("Browser parsing terminated.")

if __name__ == '__main__':
  main()
