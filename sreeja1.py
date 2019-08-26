Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("enter the value of a;")
enter the value of a;
>>> b=input("ente
	
SyntaxError: EOL while scanning string literal
>>> a=20
>>> b=30
>>> c=a+b
>>> c
50
>>> a=("python programming")
>>> a.replace("python","c")
'c programming'
>>> a=[1,2,4,8,-1,2.2,'b']
>>> a.append(5)
>>> a
[1, 2, 4, 8, -1, 2.2, 'b', 5]
>>> b=[123]
>>> a.extend(['a','b','c'])
>>> a
[1, 2, 4, 8, -1, 2.2, 'b', 5, 'a', 'b', 'c']
>>> a.extend([b])
>>> a
[1, 2, 4, 8, -1, 2.2, 'b', 5, 'a', 'b', 'c', [123]]
>>> a=['1',4,5]
>>> b=[7,8,9]
>>> a+b
['1', 4, 5, 7, 8, 9]
>>> a.index(-1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.index(-1)
ValueError: -1 is not in list
>>> a.append(-1)
>>> a
['1', 4, 5, -1]
>>> a.index(-1)
3
>>> a=["cmr","good","college"]
>>> a.insert(1,"is")
>>> a
['cmr', 'is', 'good', 'college']
>>> a.replace("college","university")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.replace("college","university")
AttributeError: 'list' object has no attribute 'replace'
>>> a.remove(3,"college")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.remove(3,"college")
TypeError: remove() takes exactly one argument (2 given)
>>> a.remove("college","university")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.remove("college","university")
TypeError: remove() takes exactly one argument (2 given)
>>> a.remove("college")
>>> a
['cmr', 'is', 'good']
>>> a.insert(3,"university")
>>> a
['cmr', 'is', 'good', 'university']
>>> a=[1,2,4,8,-1,2.2,'b',2,2]
>>> a.count(2)
3
>>> print("sreeja","7th sem","7.5")
sreeja 7th sem 7.5
>>> a
[1, 2, 4, 8, -1, 2.2, 'b', 2, 2]
>>> a=("sreeja","7thsem","7.8")
>>> print(a)
('sreeja', '7thsem', '7.8')
>>> a=[1,2,3]
>>> a=(1,2,3,"a")
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> 
