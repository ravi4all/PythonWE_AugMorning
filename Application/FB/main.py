import ReadWriteData

users = []
posts = []

# posts = [{'post':'hello everyone',
#           'date':'8/9/18','email':'ram@...'},
#          {'post': 'hello everyone',
#           'date': '8/9/18', 'email': 'ram@...'}
#          ]

def loginSuccess():
    print("""
    1. Post
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    userChoice = input("Enter your choice : ")

def post():
    pass

def updateProfile():
    pass

def deleteProfile():
    pass

def viewProfile():
    pass

def register():
    # userData = dict()
    username = input("Enter name : ")
    flag = True
    while flag:
        useremail = input("Enter email : ")
        if len(users) > 0:
            for data in users:
                if data['email'] == useremail:
                    print("EmailId Already Exist")
                    break
            else:
                flag = False
        else:
            flag = False

    userpwd = input("Enter password : ")

    # userData['name'] = username
    # userData['email'] = useremail
    # userData['password'] = userpwd

    userData = {'name' : username,
                'email' : useremail,
                'password' : userpwd}

    users.append(userData)
    # print(users)

    ReadWriteData.write_data(users)
    print("Data Stored Successfully")

def login():
    email = input("Enter emailId : ")
    pwd = input("Enter password : ")

    # for data in users:
    #     if data['email'] == email and data['password'] == pwd:
    #         print("Login Success")
    #         loginSuccess()
    #         break
    # else:
    #     print("Login Failed...")

    data = ReadWriteData.read_data()
    # print(data)
    for user in data:
        if email in user and pwd in user:
            print("Login Success")
            loginSuccess()
            break
    else:
        print("Login Failed...")

def main():
    while True:
        print("""
        1. Login
        2. Register
        """)

        userCh = input("Enter your choice : ")
        todo = {
            "1" : login,
            "2" : register
        }

        todo.get(userCh)()

main()