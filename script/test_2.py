import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
  

def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.clear()
  search_input.send_keys("Unit testing")
  search_input.submit()
  assert "Unit testing" in driver.title
  #time.sleep(5)
  searched_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "halting problem")))
  searched_link = driver.find_element_by_link_text("halting problem")  
  searched_link.click()  
  phrase_1 = driver.find_elements_by_xpath("//*[text()='Turing machine']")
  print(phrase_1)
  assert len(phrase_1) > 0
  phrase_2 = driver.find_elements_by_xpath("//*[text()='no needed']") 
  print(phrase_2)
  assert len(phrase_2) <= 0
  driver.close()


main()
  