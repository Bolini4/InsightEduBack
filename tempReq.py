import requests as r

url = "http://127.0.0.1:5000/auth/login"
data = {'email':"matteobolini@gmail.com",
        'password':'hashedpass'}
req = r.post(url,data)