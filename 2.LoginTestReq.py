import Constants 
import requests
import importJsonLog
from selenium import webdriver

def TestLogIn(email, password):
    body={
        "email":email,
        "password":password
    }
    response = requests.post('https://comtradeqa.herokuapp.com/api/users/login',data=body)
    if(response.status_code==200):
        print('Good login')
        resBody=response.status_code
        print(resBody)
    else:
        print('Bad login')
        resBody=response.status_code   
        print(resBody)

for data in importJsonLog.DATA_T:
    TestLogIn(data["email"],data["password"])

# nije neophodno ali je korisno /
# it's not necessary but it's useful
# HTTP response status codes

driver=webdriver.Chrome()
driver.get(f'{Constants.STATUS_CODE}')
driver.minimize_window()

