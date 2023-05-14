from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the form page
driver.get('https://forms.gle/Lj9RrDw9aBojc8Bx8')

time.sleep(5)
email_inp = 'Enter Email'

# Fill out the form
name_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys('Enter Name')

email_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
if re.match(email_regex, email_inp):    #   Validate Email
    print("Email is valid")
    email_field.send_keys(email_inp)
else:
    print("Email is not valid!!")       #   Invalid Email - Terminate browser and Python Script
    driver.quit()
    raise SystemExit(0)

others_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
others_field.send_keys('This is filled by Selenium!')

# Submit the form
submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()


time.sleep(2)

# Wait for the success message to appear
reply = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]')
if (reply.text == 'Your response has been recorded'):
    print("Form successfully submitted!")
else:
    print("An error occured!")

driver.quit()
