from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def setUp(self):
  self.driver = webdriver.Chrome(executable_path="bin/chromedriver")


def test_search_in_wikipedia_org(self):
  driver = self.driver
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  search_input = driver.find_element_by_id("searchInput")
  search_input.send_keys("Unit Testing")
  search_input.send_keys(Keys.ENTER)
  self.assertIn("Unit Testing", driver.title)
  searched_link = driver.find_element_by_link_text("/wiki/Halting_problem")
  phrase_1 = "Turing machine"
  phrase_2 = "no needed"
  body_text = driver.find_element_by_id("bodyContent").text
  self.assertTrue(phrase_1 in body_text)
  self.assertFalse(phrase_2 in body_text)


def tearDown(self):
  self.driver.close()
  