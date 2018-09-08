Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text = "hello this is python programming"
>>> len(text)
32
>>> text[0]
'h'
>>> text[1]
'e'
>>> text[-1]
'g'
>>> text[0:5]
'hello'
>>> text[0:4]
'hell'
>>> text[10:20]
' is python'
>>> text[0:20:2]
'hloti spto'
>>> text
'hello this is python programming'
>>> text[0:]
'hello this is python programming'
>>> text[:10]
'hello this'
>>> text[:]
'hello this is python programming'
>>> text[11:0]
''
>>> text[11:1]
''
>>> text[11:1:-1]
'i siht oll'
>>> text[11:0:-1]
'i siht olle'
>>> text[11:2]
''
>>> text[::-1]
'gnimmargorp nohtyp si siht olleh'
>>> text
'hello this is python programming'
>>> text[0:-1]
'hello this is python programmin'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-20:-1]
'rp nohtyp '
>>> text[10:0]
''
>>> text[10:0:-1]
' siht olle'
>>> text[-10:-1]
'rogrammin'
>>> text[-1:-10:-1]
'gnimmargo'
>>> text.find('p')
14
>>> text = "hello pass and python programming"
>>> text.find('p')
6
>>> text.find('python')
15
>>> text.find('programming')
22
>>> text[15:21]
'python'
>>> text = "ram is a boy, sita is a girl, shyam is also a boy"
>>> text.find('a')
1
>>> text.find('a',2)
7
>>> text.find('a',8)
17
>>> text.find('a',18)
22
>>> text.rfind('a')
44
>>> text.find('a',8,15)
-1
>>> text[8]
' '
>>> text[9]
'b'
>>> text.find('a',8,20)
17
>>> text[0] = 's'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    text[0] = 's'
TypeError: 'str' object does not support item assignment
>>> text.replace('r','s')
'sam is a boy, sita is a gisl, shyam is also a boy'
>>> text
'ram is a boy, sita is a girl, shyam is also a boy'
>>> text.replace('r','s',1)
'sam is a boy, sita is a girl, shyam is also a boy'
>>> text.upper()
'RAM IS A BOY, SITA IS A GIRL, SHYAM IS ALSO A BOY'
>>> text.lower()
'ram is a boy, sita is a girl, shyam is also a boy'
>>> text.capitalize()
'Ram is a boy, sita is a girl, shyam is also a boy'
>>> text.title()
'Ram Is A Boy, Sita Is A Girl, Shyam Is Also A Boy'
>>> text.center(50)
'ram is a boy, sita is a girl, shyam is also a boy '
>>> len(text)
49
>>> text.center(80)
'               ram is a boy, sita is a girl, shyam is also a boy                '
>>> text.center(60)
'     ram is a boy, sita is a girl, shyam is also a boy      '
>>> text.count('a')
7
>>> x = '     ram is a boy, sita is a girl, shyam is also a boy      '
>>> x
'     ram is a boy, sita is a girl, shyam is also a boy      '
>>> x.strip()
'ram is a boy, sita is a girl, shyam is also a boy'
>>> x = '--ram is a boy, sita is a girl, shyam is also a boy--'
>>> x.strip('-')
'ram is a boy, sita is a girl, shyam is also a boy'
>>> text.center(60,'*')
'*****ram is a boy, sita is a girl, shyam is also a boy******'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
