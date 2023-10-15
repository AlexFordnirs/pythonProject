Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> email = 'vasja@mail.com'
>>> print('\t')
	
>>> print('\\t')
\t
>>> print(r'\t')
\t
>>> pattern_email = r'\w+@\w+(\.\w+)+'
>>> pattern_email
'\\w+@\\w+(\\.\\w+)+'
>>> re.search(pattern_email, email)
<re.Match object; span=(0, 14), match='vasja@mail.com'>
>>> re.search(pattern_email, email) is not Null
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    re.search(pattern_email, email) is not Null
NameError: name 'Null' is not defined
>>> re.search(pattern_email, email) is not None
True
>>> re.search(pattern_email, 'mail@') is not None
False
>>> re.findall(r'\d+', 'one 1 two 2 three 3')
['1', '2', '3']
>>> re.findall('\\d+', 'one 1 two 2 three 3')
['1', '2', '3']
>>> re.search('\\d+', 'one 1 two 2 three 3')
<re.Match object; span=(4, 5), match='1'>
>>> re.find('\\d+', 'one 1 two 2 three 3')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    re.find('\\d+', 'one 1 two 2 three 3')
AttributeError: module 're' has no attribute 'find'
>>> re.search('\\d+', 'one 1 two 2 three 3')
<re.Match object; span=(4, 5), match='1'>
>>> re_email = re.compile(pattern_email)
>>> type(re_email)
<class 're.Pattern'>
>>> dir(re_email)
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
>>> re_email.pattern
'\\w+@\\w+(\\.\\w+)+'
>>> re_email.findall('Vasja vasja@mail.com Masha masha@mail.com')
['.com', '.com']
>>> re_email.search('Vasja vasja@mail.com Masha masha@mail.com')
<re.Match object; span=(6, 20), match='vasja@mail.com'>
>>> re_email.match('Vasja vasja@mail.com Masha masha@mail.com')
>>> re_email.gorups
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    re_email.gorups
AttributeError: 're.Pattern' object has no attribute 'gorups'
>>> re_email.groups
1
>>> re_email.match
<built-in method match of re.Pattern object at 0x000001BC8B19A030>
>>> re_email[1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    re_email[1]
TypeError: 're.Pattern' object is not subscriptable
>>> r = re_email.match('Vasja vasja@mail.com Masha masha@mail.com')
>>> r
>>> re_email.groups(1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    re_email.groups(1)
TypeError: 'int' object is not callable
>>> re.match(pattern_email, 'Vasja vasja@mail.com Masha masha@mail.com')
>>> re.match('\w+', 'Vasja vasja@mail.com Masha masha@mail.com')
<re.Match object; span=(0, 5), match='Vasja'>
>>> re.match(r'\w+', 'Vasja vasja@mail.com Masha masha@mail.com')
<re.Match object; span=(0, 5), match='Vasja'>
>>> m = re.match(r'\w+', 'Vasja vasja@mail.com Masha masha@mail.com')
>>> m.groups
<built-in method groups of re.Match object at 0x000001BC8D789E30>
>>> m.groups()
()
>>> m.group(0)
'Vasja'
>>> m = re.match(r'(?P<name>\w+)@(?P<domain>\w+(\.\w+)+)', 'Vasja vasja@mail.com Masha masha@mail.com')
>>> m.groups()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    m.groups()
AttributeError: 'NoneType' object has no attribute 'groups'
>>> m
>>> m = re.match(r'.*?(?P<name>\w+)@(?P<domain>\w+(\.\w+)+).*?', 'Vasja vasja@mail.com Masha masha@mail.com')
>>> m
<re.Match object; span=(0, 20), match='Vasja vasja@mail.com'>
>>> m.groups()
('vasja', 'mail.com', '.com')
>>> m.group(0)
'Vasja vasja@mail.com'
>>> m.group(1)
'vasja'
>>> m.group('name')
'vasja'
>>> 
================== RESTART: C:/Users/shaptala/Desktop/rgex.py ==================
['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua', 'Ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea', 'commodo', 'consequat', 'Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore', 'eu', 'fugiat', 'nulla', 'pariatur', 'Excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 'proident', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum']
>>> 
========= RESTART: C:/Users/shaptala/Desktop/rgex.py =========
Lorem
ipsum
dolor
sit
amet
consectetur
adipiscing
elit
sed
do
eiusmod
tempor
incididunt
ut
labore
et
dolore
magna
aliqua
Ut
enim
ad
minim
veniam
quis
nostrud
exercitation
ullamco
laboris
nisi
ut
aliquip
ex
ea
commodo
consequat
Duis
aute
irure
dolor
in
reprehenderit
in
voluptate
velit
esse
cillum
dolore
eu
fugiat
nulla
pariatur
Excepteur
sint
occaecat
cupidatat
non
proident
sunt
in
culpa
qui
officia
deserunt
mollit
anim
id
est
laborum
>>> 
========= RESTART: C:/Users/shaptala/Desktop/rgex.py =========
<re.Match object; span=(0, 5), match='Lorem'>
<re.Match object; span=(6, 11), match='ipsum'>
<re.Match object; span=(12, 17), match='dolor'>
<re.Match object; span=(18, 21), match='sit'>
<re.Match object; span=(22, 26), match='amet'>
<re.Match object; span=(28, 39), match='consectetur'>
<re.Match object; span=(40, 50), match='adipiscing'>
<re.Match object; span=(51, 55), match='elit'>
<re.Match object; span=(57, 60), match='sed'>
<re.Match object; span=(61, 63), match='do'>
<re.Match object; span=(64, 71), match='eiusmod'>
<re.Match object; span=(72, 78), match='tempor'>
<re.Match object; span=(79, 89), match='incididunt'>
<re.Match object; span=(90, 92), match='ut'>
<re.Match object; span=(93, 99), match='labore'>
<re.Match object; span=(100, 102), match='et'>
<re.Match object; span=(103, 109), match='dolore'>
<re.Match object; span=(110, 115), match='magna'>
<re.Match object; span=(116, 122), match='aliqua'>
<re.Match object; span=(124, 126), match='Ut'>
<re.Match object; span=(127, 131), match='enim'>
<re.Match object; span=(132, 134), match='ad'>
<re.Match object; span=(135, 140), match='minim'>
<re.Match object; span=(141, 147), match='veniam'>
<re.Match object; span=(149, 153), match='quis'>
<re.Match object; span=(154, 161), match='nostrud'>
<re.Match object; span=(162, 174), match='exercitation'>
<re.Match object; span=(175, 182), match='ullamco'>
<re.Match object; span=(183, 190), match='laboris'>
<re.Match object; span=(191, 195), match='nisi'>
<re.Match object; span=(196, 198), match='ut'>
<re.Match object; span=(199, 206), match='aliquip'>
<re.Match object; span=(207, 209), match='ex'>
<re.Match object; span=(210, 212), match='ea'>
<re.Match object; span=(213, 220), match='commodo'>
<re.Match object; span=(221, 230), match='consequat'>
<re.Match object; span=(232, 236), match='Duis'>
<re.Match object; span=(237, 241), match='aute'>
<re.Match object; span=(242, 247), match='irure'>
<re.Match object; span=(248, 253), match='dolor'>
<re.Match object; span=(254, 256), match='in'>
<re.Match object; span=(257, 270), match='reprehenderit'>
<re.Match object; span=(271, 273), match='in'>
<re.Match object; span=(274, 283), match='voluptate'>
<re.Match object; span=(284, 289), match='velit'>
<re.Match object; span=(290, 294), match='esse'>
<re.Match object; span=(295, 301), match='cillum'>
<re.Match object; span=(302, 308), match='dolore'>
<re.Match object; span=(309, 311), match='eu'>
<re.Match object; span=(312, 318), match='fugiat'>
<re.Match object; span=(319, 324), match='nulla'>
<re.Match object; span=(325, 333), match='pariatur'>
<re.Match object; span=(335, 344), match='Excepteur'>
<re.Match object; span=(345, 349), match='sint'>
<re.Match object; span=(350, 358), match='occaecat'>
<re.Match object; span=(359, 368), match='cupidatat'>
<re.Match object; span=(369, 372), match='non'>
<re.Match object; span=(373, 381), match='proident'>
<re.Match object; span=(383, 387), match='sunt'>
<re.Match object; span=(388, 390), match='in'>
<re.Match object; span=(391, 396), match='culpa'>
<re.Match object; span=(397, 400), match='qui'>
<re.Match object; span=(401, 408), match='officia'>
<re.Match object; span=(409, 417), match='deserunt'>
<re.Match object; span=(418, 424), match='mollit'>
<re.Match object; span=(425, 429), match='anim'>
<re.Match object; span=(430, 432), match='id'>
<re.Match object; span=(433, 436), match='est'>
<re.Match object; span=(437, 444), match='laborum'>
>>> 