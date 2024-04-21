from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.sonatech.ac.in/Results/results-sep-2023-sona-college.php")
# main_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a ")
search_button = driver.find_element(By.NAME, value="name")
search_button.send_keys("61781922111061")
dob_in = driver.find_element(By.NAME, value="dob")
dob_in.send_keys("18/09/2004")
submit_button = driver.find_element(By.NAME, value="submit")
#submit_button.click()
