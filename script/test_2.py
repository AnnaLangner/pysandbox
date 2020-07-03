import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  

def test_search_in_wikipedia_org():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.send_keys("Unit Testing")
  search_input.send_keys(Keys.ENTER)
  assertIn("Unit Testing", driver.title)
  searched_link = driver.find_element_by_link_text("/wiki/Halting_problem")
  phrase_1 = "Turing machine"
  phrase_2 = "no needed"
  body_text = driver.find_element_by_id("bodyContent").text
  assertTrue(phrase_1 in body_text)
  assertFalse(phrase_2 in body_text)
  # second way to search for a phrase
  # src = driver.page_source
  # found_phrase_1 = re.search(r"Turing machine", src)
  # assert "No result found." not in src
  driver.close()


test_search_in_wikipedia_org()
  