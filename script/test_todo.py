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


def verify_active_task(driver, label):
  elem = driver.find_element_by_xpath(f"//label[contains(text(),'{label}')]")
  class_elem = elem.get_attribute("class")
  assert class_elem != "completed"


def verify_tasks_different(driver, label1, label2):
  elem_1 = driver.find_element_by_xpath(f"//label[contains(text(),'{label1}')]")
  elem_2 = driver.find_element_by_xpath(f"//label[contains(text(),'{label2}')]")
  assert elem_1 != elem_2 


def click_task(driver, label): 
  elem_toggle = driver.find_element_by_xpath(f"//label[contains(text(),'{label}')]/preceding-sibling::input")
  elem_toggle.click()


def verify_task_completed(driver, label):
  child_elem = driver.find_element_by_xpath(f"//label[contains(text(),'{label}')]")
  parent_elem = child_elem.find_element_by_xpath("..//..")
  assert parent_elem.get_attribute("class") == "completed"


def click_button_clear_completed(driver):
  completed_button = driver.find_element_by_xpath("/html/body/section/div/footer/button")
  completed_button.click()


def verify_all_completed_task_are_deleted(driver):
  todo_list = driver.find_element_by_class_name("todo-list")
  elements = todo_list.find_elements_by_tag_name("li")
  for elem in elements:
    assert elem.get_attribute("class") != "completed"


def click_tab(driver, label):
  tab = driver.find_element_by_xpath(f"//a[contains(text(),'{label}')]")
  tab.click()


def verify_tab(driver, label):
  tab = driver.find_element_by_xpath(f"//a[contains(text(),'{label}')]")
  assert tab.get_attribute("class") == "selected"


def test_task_completed(driver):  
  add_task(driver, "task1")
  verify_active_task(driver, "task1")
  add_task(driver, "task2")
  verify_tasks_different(driver, "task1", "task2")  
  verify_active_task(driver, "task2") 
  click_task(driver, "task2")
  verify_task_completed(driver, "task2")


def test_clear_completed_task(driver):
  add_task(driver, "task3")
  add_task(driver, "task4")
  verify_active_task(driver, "task3")
  verify_active_task(driver, "task4")
  click_task(driver, "task3")
  click_button_clear_completed(driver)
  verify_all_completed_task_are_deleted(driver)


def test_switch_tabs(driver):
  add_task(driver, "task5")
  add_task(driver, "task6")
  verify_active_task(driver, "task5")
  verify_active_task(driver, "task6")
  click_task(driver, "task5")  
  verify_tab(driver, "All")
  click_tab(driver, "Active")
  verify_tab(driver, "Active")
  click_tab(driver, "Completed")  
  verify_tab(driver, "Completed")


def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("http://todomvc.com/examples/react/#/")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html/body/section/div/header/input")))
  test_task_completed(driver)
  test_clear_completed_task(driver)
  test_switch_tabs(driver)
  driver.close()


main()
