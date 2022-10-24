# Import the following modules
import selenium
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Path to downloaded chrome driver:
path = "C:\\Users\\kenny\\Downloads\\chromedriver_win32\\chromedriver.exe"

# Ask the tester a valid username and password
username = input("Please provide a valid email: ")
password = getpass()

# Start selenium chrome driver
driver = webdriver.Chrome(path)

# Go to Ace's Barbershop Website and navigate to login view and maximize the window
driver.get('http://localhost:5500/loginPage')
driver.maximize_window()
# Wait for 2 seconds
time.sleep(2)

# Log in with username and password provided by tester. After succesful login, it should navigate to Profile View with user info
driver.find_element(By.ID, 'loginpage-username').send_keys(username)
time.sleep(2)
driver.find_element(By.ID, 'loginpage-password').send_keys(password)
time.sleep(2)