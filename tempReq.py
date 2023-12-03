import requests as r

print("Press 1 for Login test")
print("Press 2 for logout test")
print("Press 3 for jwt required test")
choice = int(input("1 or 2 or 3"))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMTU5NTQzOSwianRpIjoiNWVjZTgzYTgtMjE1OS00MmYyLTlmZTgtOGFmZDVhMTgwZjBkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1hdHRlb2JvbGluaUBnbWFpbC5jb20iLCJuYmYiOjE3MDE1OTU0MzksImV4cCI6MTcwMTU5OTAzOX0.YhYLpnCrm5jmUsLgo8DqFadQ4cPtu4IVwf17diFQDjo"
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
        data = {'email':"matteobolini@gmail.com",
                'password':'hashedpass'}
        req = r.post(url,data, headers=headers)
        print(req.text)           

input("press enter to exit")