from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")


search_box01 = driver.find_element(By.ID, "username")
search_box01.send_keys("tomsmith")


search_box02 = driver.find_element(By.ID, "password")
search_box02.send_keys("SuperSecretPassword!")


driver.find_element(By.CLASS_NAME, "radius").click()


green_plashka = driver.find_element(By.ID, "flash")
tekst_plashka = green_plashka.text

print(f'Надпись на зеленой плашке: {tekst_plashka}')


driver.quit()