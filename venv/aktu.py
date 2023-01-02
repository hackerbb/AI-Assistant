from selenium import webdriver
chromedriver_location ="chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx/')
driver.implicitly_wait(10)
login = "//*[@id=\"btnSearch\"]"
captcha="/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"
audio="//*[@id=\"recaptcha-audio-button\"]"
username_input ="//*[@id=\"txtRollNo\"]"
driver.find_element_by_xpath(username_input).send_keys("1900290110046")
driver.implicitly_wait(10)
# driver.find_element_by_xpath(captcha).click()
# driver.find_element_by_xpath(audio).click()
# driver.find_element_by_xpath(login).click()
driver.find_element_by_class_name("rc-anchor rc-anchor-normal rc-anchor-light")