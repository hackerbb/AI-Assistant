from selenium import webdriver
chromedriver_location ="chromedriver"
driver = webdriver.Chrome(chromedriver_location)

driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)
first_l="//*[@id=\"react-root\"]/section/main/article/div[2]/div[2]/div/p/a/span"
login="//*[@id=\"loginForm\"]/div/div[3]"
username_input="//*[@id=\"loginForm\"]/div/div[1]/div/label/input"
password="//*[@id=\"loginForm\"]/div/div[2]/div/label/input"
driver.find_element_by_xpath(username_input).send_keys("hritik162001@gmail.com")
driver.find_element_by_xpath(password).send_keys("hritik12")
driver.find_element_by_xpath(login).click()