Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> type(d)
<class 'dict'>
>>> x = int()
>>> x
0
>>> import sys
>>> sys.getsizeof(x)
24
>>> y = 1
>>> sys.getsizeof(y)
28
>>> sys.getsizeof(d)
240
>>> d['name'] = 'Ram'
>>> d['age'] = 20
>>> d['address'] = 'Delhi'
>>> d
{'name': 'Ram', 'age': 20, 'address': 'Delhi'}
>>> sys.getsizeof(d)
240
>>> l = list()
>>> sys.getsizeof(l)
64
>>> l.append(2)
>>> sys.getsizeof(l)
96
>>> l.append('h')
>>> l
[2, 'h']
>>> sys.getsizeof(l)
96
>>> l.append(5)
>>> sys.getsizeof(l)
96
>>> l = [2,4,5,7,8,4,3,3,7,8,7,4]
>>> sys.getsizeof(l)
160
>>> d
{'name': 'Ram', 'age': 20, 'address': 'Delhi'}
>>> d.keys()
dict_keys(['name', 'age', 'address'])
>>> d['name']
'Ram'
>>> d['hobby'] = 'cricket'
>>> d
{'name': 'Ram', 'age': 20, 'address': 'Delhi', 'hobby': 'cricket'}
>>> d.get('name')
'Ram'
>>> d.items()
dict_items([('name', 'Ram'), ('age', 20), ('address', 'Delhi'), ('hobby', 'cricket')])
>>> print(d.items())
dict_items([('name', 'Ram'), ('age', 20), ('address', 'Delhi'), ('hobby', 'cricket')])
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('hobby')
'cricket'
>>> d
{'name': 'Ram', 'age': 20, 'address': 'Delhi'}
>>> d = {"name":['Ram','Shyam','Anuj','Chetan','Akshay'],'company' : []}
'
>>> 
>>> d = {"name":['Ram','Shyam','Anuj','Chetan','Akshay'],'company' : ['TCS','HCL','TCS','TCS','IBM']}
>>> d
{'name': ['Ram', 'Shyam', 'Anuj', 'Chetan', 'Akshay'], 'company': ['TCS', 'HCL', 'TCS', 'TCS', 'IBM']}
>>> 
