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


def verify_tasks_different(driver, id1, id2):
  elem_1 = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id1}]")
  elem_2 = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id2}]")
  assert elem_1.text != elem_2.text  


def click_task(driver, id):  
  elem_toggle = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]/div/input")
  elem_toggle.click()


def verify_task_completed(driver, id):
  elem = driver.find_element_by_xpath(f"/html/body/section/div/section/ul/li[{id}]")
  assert elem.get_attribute("class") == "completed"


def click_button_clear_completed(driver):
  completed_button = driver.find_element_by_xpath("/html/body/section/div/footer/button")
  completed_button.click()


def verify_all_completed_task_are_deleted(driver):
  todo_list = driver.find_element_by_class_name("todo-list")
  elements = todo_list.find_elements_by_tag_name("li")
  for elem in elements:
    assert elem.get_attribute("class") != "completed"


def click_tab(driver, id):
  tab = driver.find_element_by_xpath(f"/html/body/section/div/footer/ul/li[{id}]/a")
  tab.click()


def verify_tab(driver, id):
  tab = driver.find_element_by_xpath(f"/html/body/section/div/footer/ul/li[{id}]/a")
  assert tab.get_attribute("class") == "selected"


def test_task_completed(driver):  
  add_task(driver, "task1")
  verify_active_task(driver, 1)
  add_task(driver, "task2")
  verify_tasks_different(driver, 1, 2)  
  verify_active_task(driver, 2) 
  click_task(driver, 2)
  verify_task_completed(driver, 2)


def test_clear_completed_task(driver):
  add_task(driver, "task3")
  add_task(driver, "task4")
  verify_active_task(driver, 3)
  verify_active_task(driver, 4)
  click_task(driver, 3)
  click_button_clear_completed(driver)
  verify_all_completed_task_are_deleted(driver)


def test_switch_tabs(driver):
  add_task(driver, "task5")
  add_task(driver, "task6")
  verify_active_task(driver, 3)
  verify_active_task(driver, 4)
  click_task(driver, 3)  
  verify_tab(driver, 1)
  click_tab(driver, 2)
  verify_tab(driver, 2)
  click_tab(driver, 3)  
  verify_tab(driver, 3)


def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("http://todomvc.com/examples/react/#/")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html/body/section/div/header/input")))
  test_task_completed(driver)
  test_clear_completed_task(driver)
  test_switch_tabs(driver)
  driver.close()


main()
