from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
  command_executor='http://127.0.0.1:4000/webdriver',
  options=chrome_options
)

driver.get("https://www.example.com")
print(driver.title)
driver.quit()
