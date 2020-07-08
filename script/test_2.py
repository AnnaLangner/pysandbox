from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  

def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.clear()
  search_input.send_keys("Unit testing")
  search_input.submit()
  assert "Unit testing" in driver.title
  searched_link = driver.find_element_by_link_text("halting problem")
  driver.execute_script("arguments[0].click();", searched_link)
  phrase_1 = driver.find_elements_by_xpath("//*[text()='Turing machine']")
  print(phrase_1)
  assert len(phrase_1) > 0
  phrase_2 = driver.find_elements_by_xpath("//*[text()='no needed']") 
  print(phrase_2)
  assert len(phrase_2) <= 0
  driver.close()


main()
  