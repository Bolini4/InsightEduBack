import requests as r

print("Press 1 for Login test")
print("Press 2 for logout test")
print("Press 3 for jwt required test")
choice = int(input("1 or 2 or 3"))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMTUwODE1OCwianRpIjoiYTYzZjEwZDMtYWMzYi00NzZjLWJmMmYtMGY1OTlkNmQxMWZiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1hdHRlb2JvbGluaUBnbWFpbC5jb20iLCJuYmYiOjE3MDE1MDgxNTgsImV4cCI6MTcwMTUxMTc1OH0.ewXUudt_swsJbgVQcjybcgawpG7aVtP7J61_43UZ9Zs"
if choice == 1:
    
        url = "http://127.0.0.1:5000/auth/login"
        data = {'email':"matteobolini@gmail.com",
                'password':'hashedpass'}
        req = r.post(url,data)
        print(req.text)
elif choice == 2:
        url = "http://127.0.0.1:5000/auth/logout"
        data = {'email':"matteobolini@gmail.com",
                'password':'hashedpass'}
        req = r.post(url,data)
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