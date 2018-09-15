# Online Shopping
data = [
    {'id':101,'name':'Apple','color':'White','price':67000},
    {'id':102,'name':'Redmi','color':'Black','price':14000},
    {'id':103,'name':'Vivo','color':'Silver','price':22000},
    {'id':104,'name':'Vivo','color':'White','price':25500},
    {'id':105,'name':'Apple','color':'Silver','price':90000},
    {'id':106,'name':'Redmi','color':'Black','price':13000},
    {'id':107,'name':'Oppo','color':'White','price':21000},
    {'id':108,'name':'Oppo','color':'White','price':20000},
    {'id':109,'name':'Apple','color':'Black','price':55000},
    {'id':110,'name':'Samsung','color':'Black','price':58000},
    {'id':111,'name':'Samsung','color':'Silver','price':36000},
    {'id':112,'name':'Samsung','color':'White','price':45000},
    {'id':113,'name':'Vivo','color':'White','price':25000},
]

# p_name = input("Enter the name of product : ")

# for product in data:
#     if product['name'].lower() == p_name.lower():
#         print(product)

# for i in range(len(data)):
#     if data[i]['name'].lower() == p_name.lower():
#         print(data[i])

print("""
1. 1000 - 10,000
2. 10,000 - 20,000
3. 20,000 - 30,000
4. 30,000 and above
""")

userChoice = input("Enter your price range : ")
if userChoice == "2":
    for p in data:
        if p['price'] < 20000 and p['price'] > 10000:
            print(p)