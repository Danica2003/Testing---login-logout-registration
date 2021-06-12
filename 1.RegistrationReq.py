
import requests
import importJsonReg

def Registration(email, password, username):
    body={
        "email":email,
        "password":password,
        "username":username
    }
    response = requests.post('https://comtradeqa.herokuapp.com/api/users/add',data=body)
    if(response.status_code==201):
        print('Sucessful registration')
        resBody=response.status_code
        print(resBody)
    elif response.status_code==409:
        print('The user already exists in the database')
        resBody=response.status_code   
        print(resBody)
    else:
        print('registration error')
        resBody=response.status_code
        print(resBody)

for data in importJsonReg.DATA:
    Registration(data["email"],data["password"],data["username"])


