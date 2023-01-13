from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time

# Opens up a Chrome webdriver
driver = webdriver.Chrome('C:/chromedriver.exe')

# Goes to google images
driver.get('https://images.google.com/')

# Modify this list according to your needs
img_list = ["apples", "bananas", "pineapples", "strawberries"]

# Finds the google search bar using xpath
search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# Using the search bar to send keywords
search_bar.send_keys('token' + ' coinmarketcap')
search_bar.send_keys(Keys.ENTER)

# Click on 'Tools'
tools = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div')
tools.click()

# Click on 'Colour'
color = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[2]/div/div[1]')
color.click()

# Click on 'Transparent' (to only get transparent images)
trans = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[3]/div/span')
trans.click()

# Loop through the items in token_list
for i in img_list:

    # Finds the google search bar using xpath
    search = driver.find_element(By.XPATH, '//*[@id="REsRA"]')

    # Clears previous input
    search.clear()

    # Using the search bar to send keywords
    search.send_keys(i + '' + 'png')
    search.send_keys(Keys.ENTER)

    # Waits for 1 second
    time.sleep(1)

    # Click on 'Tools'
    tools = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div')
    tools.click()

    # Click on 'Colour'
    color = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[2]/div/div[1]')
    color.click()

    # Click on 'Transparent'
    trans = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[3]/div/span')
    trans.click()

    # Finds and clicks on the first image
    try:
        first_img = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]')
        first_img.click()
    except:
        print("Line 52 error: " + str(i) + " unable to download")
        pass

    # Wait for 2 seconds
    time.sleep(2)

    # Grabs the img xpath
    try:
        token_img = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
    except:
        print("Line 63 error: " + str(i) + " unable to download")
        pass

    # Grabs the image source
    src = token_img.get_attribute('src')

    # Downloads the image
    try:
        urllib.request.urlretrieve(src, i + ".png")
    except:
        print("Line 73 error: " + str(i) + " unable to download")
        pass
