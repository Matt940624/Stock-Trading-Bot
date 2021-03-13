from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.dailyfxasia.com/cn/forex-rates")

js = ""
with open("main.js", "r") as f:
    js = f.read()

while True:
    try:
        driver.execute_script(js)
        break
    except:
        pass
    pass


import socket_server
