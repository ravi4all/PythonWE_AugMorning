Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = [1,2,3,4,5,'hello','bye',10.55,True]
>>> data[0]
1
>>> data[-1]
True
>>> data[0:4]
[1, 2, 3, 4]
>>> data[4:0:-1]
[5, 4, 3, 2]
>>> data[0] = 0
>>> data
[0, 2, 3, 4, 5, 'hello', 'bye', 10.55, True]
>>> data[0:3] = [9,8,7]
>>> data
[9, 8, 7, 4, 5, 'hello', 'bye', 10.55, True]
>>> dir(data)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append(2)
>>> 
>>> data
[2]
>>> data.append(4)
>>> data
[2, 4]
>>> data.append(6,8,10,12)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data.append(6,8,10,12)
TypeError: append() takes exactly one argument (4 given)
>>> data = []
>>> for i in range(1,51):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data.pop()
50
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data.index(20)
9
>>> data.pop(9)
20
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data.insert(9,20)
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data_2 = []
>>> for i in range(1,11):
	data_2.append(i ** 2)

	
>>> data_2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data_2 = [i for i in range(1,11)]
>>> data_2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data_2 = [i**2 for i in range(1,11)]
>>> data_2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data_2 = [i for i in range(1,51) if i % 2 == 0]
>>> data_2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data_2 = [i**2 for i in range(1,11)]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data_2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data + data_2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data.append(data_2)
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]]
>>> data[-1]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data.pop()
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data.extend(data_2)
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> sorted(data)
[1, 2, 4, 4, 6, 8, 9, 10, 12, 14, 16, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 36, 38, 40, 42, 44, 46, 48, 49, 64, 81, 100]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data.sort()
>>> data
[1, 2, 4, 4, 6, 8, 9, 10, 12, 14, 16, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 36, 38, 40, 42, 44, 46, 48, 49, 64, 81, 100]
>>> data.count(4)
2
>>> data.remove(7)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    data.remove(7)
ValueError: list.remove(x): x not in list
>>> data.remove(4)
>>> data
[1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 36, 38, 40, 42, 44, 46, 48, 49, 64, 81, 100]
>>> del data[10]
>>> data
[1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 36, 38, 40, 42, 44, 46, 48, 49, 64, 81, 100]
>>> user = "ram"
>>> print
<built-in function print>
>>> print("hello",user)
hello ram
>>> 15 / 7
2.142857142857143
>>> 15 // 7
2
>>> data = [['Ram','Shyam','Mohan','Aman','Javed'],[89,78,76,70,45]]
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed'], [89, 78, 76, 70, 45]]
>>> data[0]
['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed']
>>> data[1]
[89, 78, 76, 70, 45]
>>> data[0].append('Anuj')
>>> data[1].append(57)
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57]]
>>> print(data[0][0], data[1][0])
Ram 89
>>> print(data[0][1], data[1][1])
Shyam 78
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i])

	
Ram 89
Shyam 78
Mohan 76
Aman 70
Javed 45
Anuj 57
>>> data.append('Delhi')
>>> data.append('Pune')
>>> data.append('Punjab')
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Punjab']
>>> t = [1,2,3,4,5,6]
>>> x = t
>>> x
[1, 2, 3, 4, 5, 6]
>>> t
[1, 2, 3, 4, 5, 6]
>>> x[0] = 100
>>> x
[100, 2, 3, 4, 5, 6]
>>> t
[100, 2, 3, 4, 5, 6]
>>> id(t)
1507293236616
>>> id(x)
1507293236616
>>> t == x
True
>>> t is x
True
>>> y = t[:]
>>> y
[100, 2, 3, 4, 5, 6]
>>> t
[100, 2, 3, 4, 5, 6]
>>> y == t
True
>>> y is t
False
>>> t[0] = 0
>>> t
[0, 2, 3, 4, 5, 6]
>>> y
[100, 2, 3, 4, 5, 6]
>>> x
[0, 2, 3, 4, 5, 6]
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Punjab']
>>> data_copy1 = data[:]
>>> data[-1] = 'Haryana'
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> data_copy1
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Punjab']
>>> data[0][0] = 'Krishna'
>>> data
[['Krishna', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> data_copy1
[['Krishna', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Punjab']
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> z = copy.deepcopy(data)
>>> z
[['Krishna', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> data
[['Krishna', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> data[0][0] = 'Ram'
>>> data
[['Ram', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> z
[['Krishna', 'Shyam', 'Mohan', 'Aman', 'Javed', 'Anuj'], [89, 78, 76, 70, 45, 57], 'Delhi', 'Pune', 'Haryana']
>>> 
