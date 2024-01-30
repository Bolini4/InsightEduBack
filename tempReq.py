import requests as r

print("Press 1 for Login test")
print("Press 2 for logout test")
print("Press 3 for jwt required test")
choice = int(input("1 or 2 or 3"))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjYxODc3MCwianRpIjoiZGVjOTcxMmQtYzgwZC00MDM1LTlkNzMtMWE4N2RiNDA3Zjg0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1hdHRlb2JvbGluaUBnbWFpbC5jb20iLCJuYmYiOjE3MDY2MTg3NzAsImV4cCI6MTcwNjYyMjM3MH0.GgkmM5kH1li_nUIDK_VM-P8CUGohLnF0IjfpFAYDGY0"


if choice == 1:
    
        url = "http://127.0.0.1:5000/auth/login"
        data = {'email':"matteobolini@gmail.com",
                'password':'hashedpass'}
        req = r.post(url,data)
        print(req.text)
elif choice == 2:
        headers = {
    "Authorization": f"Bearer {token}"
}
        url = "http://127.0.0.1:5000/auth/logout"
        data = {'email':"matteobolini@gmail.com",
                'password':'hashedpass'}
        req = r.post(url,headers=headers)
        print(req.text)
elif choice == 3:
        headers = {
    "Authorization": f"Bearer {token}"
}
        url = "http://127.0.0.1:5000/"
        data = {'email':"bolinettemail@google.com",
                'password':'password'}
        req = r.post(url,data, headers=headers)
        print(req.text)           

input("press enter to exit")