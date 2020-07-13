from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException


def add_task(driver, title):
  input_todo = driver.find_element_by_xpath("//html/body/section/div/header/input")
  input_todo.clear()
  input_todo.send_keys(title)
  input_todo.send_keys(Keys.RETURN)


def active_task(driver, id):
  elem = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[%s]"%str(id))
  try:
    class_elem = elem.get_attribute("class")
    if(class_elem == "completed"):
      return True
  except:
    NoSuchAttributeException


def comparison_of_adjacent_tasks(driver, id):
  elem_1 = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[%s]"%str(id))
  elem_2 = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[%s]"%str(id+1))
  if(elem_1.text != elem_2.text):
    pass
  else:
    print("You already have this task")


def task_completed(driver, id):
  elem = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[%s]"%str(id))
  elem_toggle = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[%s]/div/input"%str(id))
  elem_toggle.click()
  assert elem.get_attribute("class") == "completed"



def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("http://todomvc.com/examples/react/#/")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html/body/section/div/header/input")))
  add_task(driver, "task1")
  active_task(driver, 1)
  add_task(driver, "task2")
  comparison_of_adjacent_tasks(driver, 1)  
  active_task(driver, 2) 
  task_completed(driver, 2)
  driver.close()


main()
