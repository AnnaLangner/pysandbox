from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  

def main():
  driver = webdriver.Firefox(executable_path="bin/geckodriver.exe")
  # driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.clear()
  search_input.send_keys("Unit testing")
  search_input.submit()
  time.sleep(3)
  assert "Unit testing" in driver.title
  searched_link = driver.find_element_by_link_text("halting problem")
  driver.execute_script("arguments[0].click();", searched_link)
  time.sleep(3)
  phrase_1 = driver.find_elements_by_xpath("//*[text()='Turing machine']")
  assert len(phrase_1) > 0
  phrase_2 = driver.find_elements_by_xpath("//*[text()='no needed']") 
  assert len(phrase_2) == 0
  driver.close()


main()
  