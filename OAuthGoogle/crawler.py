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
    default='foo@example.com',
    help='Your site ID.')
  parser.add_argument(
    '--passwd',
    type=str,
    default='passwd',
    help='Your site password.')

  FLAGS, unparsed = parser.parse_known_args()

  options = webdriver.ChromeOptions()
  # Headless option
  options.add_argument('headless')
  options.add_argument('window-size=1920x1080')
  options.add_argument("disable-gpu")

  browser = webdriver.Chrome(FLAGS.chromedriver, chrome_options=options)
  browser.implicitly_wait(3)

  browser.get(FLAGS.site)
  browser.find_element_by_xpath('//*[@id="google-signin-button"]').click()
  title = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "head > title")))

  wait = WebDriverWait(browser, 20)
  presence = EC.presence_of_element_located
  visible = EC.visibility_of_element_located

  wait.until(presence((By.ID, 'identifierId')))
  browser.find_element_by_id('identifierId').send_keys(FLAGS.id)
  browser.find_element_by_id("identifierNext").click()

  wait.until(presence((By.ID, 'password')))
  browser.find_element_by_name('password').send_keys(FLAGS.passwd)
  element = browser.find_element_by_id('passwordNext')
  browser.execute_script("arguments[0].click();", element)

  # FIXME.
  wait.until(presence((By.ID, 'title-text')))

  html = browser.page_source
  soup = BeautifulSoup(html, 'html.parser')
  browser.quit()

if __name__ == '__main__':
  main()
