from selenium import webdriver
import Constants
import Locators
import time

def LogIn(email,password):
    driver = webdriver.Chrome()
    driver.get(f"{Constants.BASE_URL}")
    driver.maximize_window()

    loginButton = driver.find_element_by_css_selector(Locators.log_dugme_prijavi_se_css_s)
    loginButton.click()

    emailField = driver.find_element_by_css_selector(Locators.log_polje_imejl_css_s)
    passwordField  = driver.find_element_by_css_selector(Locators.log_polje_sifra_css_s)

    emailField.send_keys(email)
    passwordField.send_keys(password)

    logInPotvrdiButton = driver.find_element_by_css_selector(Locators.log_dugme_uloguj_se_css_s)
    logInPotvrdiButton.click()

    logOutButton = driver.find_element_by_css_selector(Locators.log_dugme_odjavi_se_css_s)
    logOutButton.click()
    time.sleep(1)
    
    if(driver.current_url=="https://comtradeqa.herokuapp.com/"):
        print('Successfully logged out')
    else:
        print('Unsuccessfully logged out')
    time.sleep(3)
# url bug
    if(driver.current_url=="https://comtradeqa.herokuapp.com"):
        print('Successfully logged out')
    else:
        print('Unsuccessfully logged out')
    time.sleep(3)


LogIn("ncocozza0@guardian.co.uk","8qRh83jtBUu")



