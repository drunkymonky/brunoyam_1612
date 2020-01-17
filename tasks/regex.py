import re

pattern = re.compile('^world')
value = 'world, hello something'
print(re.search(pattern, value))

pattern = re.compile('^\w\w\w$')
print(re.search(pattern, 'abF'))
print(re.search(pattern, "asfdfs"))

pattern = re.compile('\d\d\d')
print(re.search(pattern, 'Hello 42323'))

pattern = re.compile('^Hello,\s\w\w\w\w!')
print(re.search(pattern, 'Hello, Svet!'))

pattern = re.compile('^\d{4}$')
print(re.search(pattern, '1234'))
print(re.search(pattern, '12345'))

pattern = re.compile('^\d{4,10}$')
print(re.search(pattern, '123'))

pattern = re.compile('^\d{4,}$')
print(re.search(pattern, '123123123123123'))

pattern = re.compile('^\d\{3,4}$')
print(re.search(pattern, '1{3,4}'))

pattern = re.compile('^[abc]+$')
print(re.search(pattern, 'abababccbacbabcab'))
print(re.search(pattern, 'abababccbacbabcabe'))

pattern = re.compile('^[0-5]+$')
pattern = re.compile('^[b-z]+$')

pattern = re.compile('^(hello|world|something)$')


#1 DD.MM.YYYY
# 12.12.1200 - OK
# 45.17.1230 - FAIL

# (3[01]|[012]\d)\. to be continued

#2 +7xxx-xxx-xx-xx
# +7999888-77-66 - OK
# +89999992233 - FAIL
# \+7-?\d{3}-?\d{3}-?\d{2}-?\d{2}
pattern = re.compile('(?:0[1-9]|[12]\d|3[01])\.(0[1-9]|1[012])\.(\d{4})')
result = re.search(pattern, '12.10.2020 date')
print(result.groups())
print(result.group(1))
print(result.group(0))

# Четное число
# [02468]$

# Шестнадцатиричная запись цвета
# #FF42A5  0-9 A-F
# #(\d|[A-F]){6}

pattern = re.compile('hello', re.IGNORECASE | re.A)
print(re.search(pattern, "helLO"))

print(re.match(pattern, 'hello'))
print(re.match(pattern, 'hello'))
print(re.findall(pattern, 'hello'))
print(re.sub('\s+', ' ', 'Hello     world      it\'s    me'))

