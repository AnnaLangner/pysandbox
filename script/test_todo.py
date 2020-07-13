from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_task(driver, title):
  input_todo = driver.find_element_by_xpath("//html/body/section/div/header/input")
  input_todo.clear()
  input_todo.send_keys(title)
  input_todo.send_keys(Keys.RETURN)


def verify_active_task(driver, id):
  elem = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]")
  class_elem = elem.get_attribute("class")
  assert class_elem != "completed"


def verify_comparison_of_adjacent_tasks(driver, id):
  elem_1 = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]")
  elem_2 = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}+{1}]")
  assert elem_1.text != elem_2.text  


def click_on_input_task_completed(driver, id):  
  elem_toggle = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]/div/input")
  elem_toggle.click()


def verify_task_completed(driver, id):
  elem = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]")
  assert elem.get_attribute("class") == "completed"



def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("http://todomvc.com/examples/react/#/")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html/body/section/div/header/input")))
  add_task(driver, "task1")
  verify_active_task(driver, 1)
  add_task(driver, "task2")
  verify_comparison_of_adjacent_tasks(driver, 1)  
  verify_active_task(driver, 2) 
  click_on_input_task_completed(driver, 2)
  verify_task_completed(driver, 2)
  driver.close()


main()