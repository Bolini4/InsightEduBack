import requests as r

print("Press 1 for Login test")
print("Press 2 for logout test")
print("Press 3 for jwt required test")
choice = int(input("1 or 2 or 3"))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNDg3OTA5NiwianRpIjoiNDI0MDk3YTItN2Y0OS00N2ExLWE5ZjgtM2Q3NjRiNDA0YjViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImJvbGluZXR0ZW1haWxAZ29vZ2xlLmNvbSIsIm5iZiI6MTcwNDg3OTA5NiwiZXhwIjoxNzA0ODgyNjk2fQ.nePrt07a84HkcVxpt_uV_7WLDEdncOE-kUJzjPbHh3Q"


if choice == 1:
    
        url = "http://127.0.0.1:5000/auth/login"
        data = {'email':"bolinettemail@google.com",
                'password':'password'}
        req = r.post(url,data)
        print(req.text)
elif choice == 2:
        headers = {
    "Authorization": f"Bearer {token}"
}
        url = "http://127.0.0.1:5000/auth/logout"
        data = {'email':"bolinettemail@google.com",
                'password':'password'}
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