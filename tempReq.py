import requests as rtemp

url = "http://127.0.0.1:5000/auth/login"
data = {'email':"matteobolini@gmail.com",
        'password':'hashedpass'}
req = r.post(url,data)

input("press enter to exit")