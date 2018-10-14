def atm():
    total = 10000
    pin = input("Enter PIN : ")

    if pin == "1234":
        print("Login Success")
    else:
        # print("Login failed")
        raise ValueError("Login Failed")

    withdraw = int(input("Enter amount to withdraw : "))
    assert (withdraw < total), "Not enough balance"
    total -= withdraw
    print("Transaction Successfull")

try:
    atm()
except ValueError as err:
    print(err)
except AssertionError as err:
    print(err)