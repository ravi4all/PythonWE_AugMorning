Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> x = 10,
\
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x
(10,)
>>> x = (10,12,2,45,22)
>>> x = 10,23,44,56
>>> emp = name, age, sal = 'Ram', 30, 25000
>>> emp
('Ram', 30, 25000)
>>> name
'Ram'
>>> age
30
>>> sal
25000
>>> emp
('Ram', 30, 25000)
>>> a,b,c = emp
>>> a
'Ram'
>>> b
30
>>> c
25000
>>> id(name)
2661506866232
>>> id(a)
2661506866232
>>> 
