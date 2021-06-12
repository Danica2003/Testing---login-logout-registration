import requests
import Constants

def isOnline(Url):
    response = requests.get(Url)
    if(response.status_code==200):
        return True
    else:
        return False

if(isOnline(Constants.BASE_URL)==True):
    print('Website is online')
else:
    print('Website is not online')

if(isOnline(Constants.BASE_URL2)==True):
    print('Website2 is online')
else:
    print('Website2 is not online')

if(isOnline(f"{Constants.BASE_URL}{Constants.LOGIN_URL}")==True):
    print('Login page is online')
else:
    print('Login page is not online')

if(isOnline(f"{Constants.BASE_URL}{Constants.BASE_REGISTRATION_URL}")==True):
    print('Registration page is online')
else:
    print('Registration page is not online')

if(isOnline(Constants.LOGIN2_URL)==True):
    print('Login2 is online')
else:
    print('Login2 is not online')

if(isOnline(Constants.BASE_REGISTRATION2_URL)==True):
    print('Registration2 is online')
else:
    print('Registration2 is not online')