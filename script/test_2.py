from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  

def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.clear()
  search_input.send_keys("Unit Testing")
  search_input.submit()
  if "Unit Testing" in driver.current_url:
    print("We are on a good site")
  searched_link = driver.find_element_by_link_text("halting problem")
  searched_link.click()
  content_page = driver.find_element_by_id('content')
  src = driver.page_source
  driver.find_elements_by_xpath("//*[contains(text(), 'Turing machine')]")  
  assert "No result found." not in src
  driver.find_elements_by_xpath("//*[contains(text(), 'no needed')]")  
  assert "No result found." not in src
  driver.close()


main()
  