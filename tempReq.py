import requests as r

print("Press 1 for Login test")
print("Press 2 for logout test")
print("Press 3 for jwt required test")
choice = int(input("1 or 2 or 3"))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNDUzMjQ2MCwianRpIjoiZTI2ZTg0NDMtZTZhNS00MGQ2LTgzMzEtM2FjNzMzNDUwNDlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1hdHRlb2JvbGluaUBnbWFpbC5jb20iLCJuYmYiOjE3MDQ1MzI0NjAsImV4cCI6MTcwNDUzNjA2MH0.Hg1ISZYt0WiefqCwvZUXCTmItXs7tnEAHUk87ZQDYy8"


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