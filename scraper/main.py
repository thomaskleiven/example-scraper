import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from pathlib import Path

from scraper.helpers import download_assets

# Reshape Credentials
username = "foo"
password = "bar"

####################
# Initiate the Chrome browser
####################
driver = webdriver.Chrome()

# Head to the reshape login homepage
driver.get("https://ris.reshapebiotech.com/auth/login")

####################
# Log In
####################

# Find the username field by name
username_field = driver.find_element(
    By.XPATH, "//input[contains(@placeholder,'Email')]"
)

# Find the password field by name
password_field = driver.find_element(
    By.XPATH, "//input[contains(@placeholder,'Password')]"
)

# Send the username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Find the submit button using xpath
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

####################
# Download Image (Best Case)
####################

# Find image by xpath
image_element = driver.find_element(By.XPATH, "//img[@alt='Reshape logo']")

# Get the image url
image_url = image_element.get_attribute("src")

# Download the image
response = requests.get(image_url)

# NB! Adapt the filename to the image type
with open("image.svg", "wb") as file:
    file.write(response.content)

####################
# Download Image (Second Best Case)
####################

# Download content to temp folder
# NB! this downloads all assets
asset_dir = "data"
Path(asset_dir).mkdir(parents=True, exist_ok=True)

time.sleep(1)
download_assets(driver.requests, asset_dir=asset_dir)

####################
# Download Image (Worst Case)
####################

with open("filename.png", "wb") as file:
    file.write(image_element.screenshot_as_png)
