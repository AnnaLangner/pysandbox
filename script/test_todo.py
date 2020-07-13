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


def main():
  driver = webdriver.Chrome(executable_path="bin/chromedriver")
  driver.get("http://todomvc.com/examples/react/#/")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html/body/section/div/header/input")))
  add_task(driver, "task1")
  elem_1 = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[1]")
  try:
    class_1 = elem_1.get_attribute("class")
    if(class_1 == "completed"):
      return True
  except:
    NoSuchAttributeException 
  add_task(driver, "task2")
  elem_2 = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[2]")
  if(elem_1.text != elem_2.text):
    pass
  else:
    print("You already have this task")
  try:
    class_2 = elem_2.get_attribute("class")
    if(class_2 == "completed"):
      return True
  except:
    NoSuchAttributeException 
  elem_2_toggle = driver.find_element_by_xpath("/html/body/section/div/section/ul/li[2]/div/input")
  elem_2_toggle.click()
  assert elem_2.get_attribute("class") == "completed"    
  driver.close()


main()
