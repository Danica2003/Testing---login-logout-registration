from selenium import webdriver
import Constants
import Locators
import time
import importJsonLog


driver = webdriver.Chrome()    

def LogIn(email,password):
    driver = webdriver.Chrome()
    driver.get(f"{Constants.BASE_URL}") #{Constants.LOGIN_URL}" not found

    loginButton = driver.find_element_by_css_selector(Locators.log_dugme_prijavi_se_css_s)
    loginButton.click()

    emailField = driver.find_element_by_css_selector(Locators.log_polje_imejl_css_s)
    passwordField  = driver.find_element_by_css_selector(Locators.log_polje_sifra_css_s)

    emailField.send_keys(email)
    passwordField.send_keys(password)

    logInPotvrdiButton = driver.find_element_by_css_selector(Locators.log_dugme_uloguj_se_css_s)
    logInPotvrdiButton.click()
    
# ne ispisuje a loguje korisnika za "https://comtradeqa.herokuapp.com"
    if(driver.current_url==f"{Constants.BASE_URL}"): # the site has no end of point url
        print(f"Sucessfull login with {email} and {password}")
    else:
        print(f"Bad login for {email} and {password}")
    time.sleep(3)

# u printu ispisiju uspesan login za "https://comtradeqa.herokuapp.com/"
    if(driver.current_url==f"{Constants.BASE_URL2}"): # the site has no end of point url+/
        print(f"Sucessfull login with {email} and {password}")
    else:
        print(f"Bad login for {email} and {password}")
    time.sleep(3)


for data in importJsonLog.DATA_T:
    LogIn(data["email"],data["password"])
