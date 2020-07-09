import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
  

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--driver', help='entry driver')
  args = parser.parse_args() 
  driver_choice = args.driver  
  if driver_choice == 'chrome':
    driver = webdriver.Chrome(executable_path="bin/chromedriver")
  else:
    driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.clear()
  search_input.send_keys("Unit testing")
  search_input.submit()
  WebDriverWait(driver, 10).until(EC.title_contains("Unit testing"))
  assert "Unit testing" in driver.title
  searched_link = driver.find_element_by_link_text("halting problem")
  driver.execute_script("arguments[0].click();", searched_link)
  WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="bodyContent"]'), 'Turing machine'))
  phrase_1 = driver.find_elements_by_xpath("//*[text()='Turing machine']")
  assert len(phrase_1) > 0
  phrase_2 = driver.find_elements_by_xpath("//*[text()='no needed']") 
  assert len(phrase_2) == 0
  driver.close()


main()
  