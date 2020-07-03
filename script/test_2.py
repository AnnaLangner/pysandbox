import re
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
  phrase_1 = "Turing machine"
  phrase_2 = "no needed"
  src = driver.page_source
  found_phrase_1 = re.search(phrase_1, src)  
  assert "No result found." not in src
  found_phrase_2 = re.search(phrase_2, src)
  assert "No result found." in src
  driver.close()


main()
  