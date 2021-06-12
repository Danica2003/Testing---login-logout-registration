from selenium import webdriver
import Constants
import Locators
import time
import ImpJsonReg2
import requests
driver = webdriver.Chrome()

def Registration1(username,email,password1,password2):
    driver = webdriver.Chrome()
    driver.get(f"{Constants.BASE_URL}")

    loginButton = driver.find_element_by_css_selector(Locators.log_dugme_prijavi_se_css_s)
    loginButton.click()

    regButton = driver.find_element_by_css_selector(Locators.reg_dugme_registruj_se1_css_s)
    regButton.click()

    korisnickoImePolje = driver.find_element_by_css_selector(Locators.reg_polje_korisnicko_ime_css_s)
    emailpolje = driver.find_element_by_css_selector(Locators.reg_polje_imejl_css_s)
    password1polje = driver.find_element_by_css_selector(Locators.reg_polje_sifra_css_s)
    password2polje = driver.find_element_by_css_selector(Locators.reg_polje_potvrdi_sifru_css_s)

    korisnickoImePolje.send_keys(username)
    emailpolje.send_keys(email)
    password1polje.send_keys(password1)
    password2polje.send_keys(password2)

    regButtonPotvrdipodatke= driver.find_element_by_css_selector(Locators.reg_dugme_registruj_se2_css_s)
    regButtonPotvrdipodatke.click()

    regButton2 = driver.find_element_by_css_selector(Locators.reg__dugme_potvrdi_registruj_se_css_s)
    regButton2.click()

    if(driver.current_url==f"{Constants.LOGIN2_URL}"): 
        print(f"Sucessfull login with {email} and {password1}")
    else:
        print(f"Bad login for {email} and {password1}")
    time.sleep(3)

for data in ImpJsonReg2.DATA_R:
    Registration1(data["username"],data["email"],data["password1"],data["password2"])

