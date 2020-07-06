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
  searched_link.click()
  driver.find_elements_by_xpath("//*[contains(text(), 'Turing machine')]")  
  assert "Turing machine"
  driver.find_elements_by_xpath("//*[contains(text(), 'no needed')]") 
  assert "no needed"
  driver.close()


main()
  