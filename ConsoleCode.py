Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 12
>>> a + b
22
>>> a - b
-2
>>> a / b
0.8333333333333334
>>> a * b
120
>>> a = "hello world"
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/FirstCode.py 
Sum is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/FirstCode.py 
Sum is 22
Sum of a and b is c
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/FirstCode.py 
Sum is 22
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/FirstCode.py 
Sum is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/FirstCode.py 
Sum is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
>>> a = "hello {}".format("ram")
>>> a
'hello ram'
>>> name = "ram"
>>> a = "hello {}".format(name)
>>> a
'hello ram'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/August_2018/PythonWE_Morning/InputFunction.py 
Enter your name : ram
Hello ram
>>> import sys
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = 10
>>> type(a)
<class 'int'>
>>> sys.getsizeof(a)
28
>>> a = 10000000
>>> sys.getsizeof(a)
28
>>> sys.getsizeof(int())
24
>>> a = 0
>>> sys.getsizeof(a)
24
>>> a = 1
>>> sys.getsizeof(a)
28
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> sys.getsizeof(a)
24
>>> sys.getsizeof(float())
24
>>> a = 12
>>> b = 5
>>> a/b
2.4
>>> a//b
2
>>> 
