#built in datatypes
a = 'hello' #string
b = 10 #integer
c = 10.5 #float
d = True #boolean
e = None #NoneType
f = [1,2,3] #list
g = (1,2,3) #tuple
h = {'one':1,'two':2,'three':3} #dictionary

#create built in datatypes
i = str('hello')
j = int(10)
k = float(10.5)
l = bool(True)
m = list([1,2,3])
n = tuple((1,2,3))
o = dict(one=1,two=2,three=3)

#see values of built in datatypes
print(a.__class__)
print(b.__class__)
print(c.__class__.__class__)

#some methods of built in datatypes
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a.find('e'))
print(a.replace('e','a'))
print(a.split('e'))
print(a.strip('h'))
print(a.isalpha())
print(a.isnumeric())
print(a.isalnum())
print(a.startswith('h'))
print(a.endswith('o'))
print(a.join('123'))
print(a.count('l'))
print(a.index('l'))
print(a[0])
print(a[1:3])
print(a[1:])
print(a[:3])
print(a[::-1])
print(a[::2])
print(a[-1])
print(a[-3:-1])
print(a[-3:])
print(a[:-3])
print(a[-1:-3])