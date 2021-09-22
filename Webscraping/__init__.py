from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(r'C:\Users\logan\Documents\chromedriver.exe')

driver.maximize_window()
driver.get("https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-1-Pack/dp/B014I8TC4E/ref=sr_1_1_sspa?crid=XBIKJ0KVWSMF&dchild=1&keywords=hdmi+cable&qid=1590703769&sprefix=hdmi+%2Caps%2C240&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSRUZQNjRRSlhWTFkmZW5jcnlwdGVkSWQ9QTA0NjU0NTczQldDSDFNM1FMVU5TJmVuY3J5cHRlZEFkSWQ9QTAxMDc0MjgzRUdSRUozMTlNOVpVJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")

amazon_price = driver.find_element_by_id("priceblock_ourprice")
price = amazon_price.text
driver.close()
print(price)

