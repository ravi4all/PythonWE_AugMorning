Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> file = open('Text_1.txt')
>>> file.read()
''
>>> file.close()
>>> file = open('Text_1.txt','w')
>>> file.write("hello world")
11
>>> file.close()
>>> file.read()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    file.read()
ValueError: I/O operation on closed file.
>>> file = open('Text_1.txt')
>>> file.write("bye world")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    file.write("bye world")
io.UnsupportedOperation: not writable
>>> file.read()
'hello world'
>>> file.close()
>>> file = open('file_12.txt','w')
>>> file.write('this file is created by python script')
37
>>> file.close()
>>> import os
>>> os.getcwd()
'C:\\Python36'
>>> os.mkdir('python_1')
>>> os.rmdir('python_1')
>>> os.remove('file_12.txt')
>>> os.startfile('dhoni.mp4')
>>> import glob
>>> glob.glob("*.txt")
['file_1.txt', 'LICENSE.txt', 'obj.txt', 'Text_1.txt', 'Text_2.txt', 'Text_3.txt', 'write_bin.txt', 'write_bin_2.txt']
>>> file = open('file_12.txt','a')
>>> file.write("this file is created by python script")
37
>>> file.close()
>>> file = open('file_12.txt')
>>> file.read()
'this file is created by python script'
>>> file.close()
>>> file = open('file_12.txt','a')
>>> file.write("now this data is appended")
25
>>> file.close()
>>> file = open('file_12.txt')
>>> file.read()
'this file is created by python scriptnow this data is appended'
>>> file.close()
>>> file = open('file_12.txt','w')
>>> file.write("now this data is new")
20
>>> file.close()
>>> file = open('file_12.txt')
>>> file.read()
'now this data is new'
>>> file.close()
>>> file = open('example_1.html','w')
>>> file.write("<h1>Hello world</h1>")
20
>>> file.close()
>>> os.startfile('example_1.html')
>>> 
