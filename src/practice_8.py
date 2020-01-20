import re
pattern = re.compile('<b>(.+?)<\/b>')
value = "<b> hello world </b><b> dsfsf </b>"
print(re.sub(pattern, '*\\1*', value))

pattern = re.compile('(\w+)(\s+\\1)+')
value = "abc abc abc def def def def def def"
print(re.sub(pattern, '\\1', value))

pattern = re.compile('^[a-zA-Z]\w*(\d\w*[!?]|[!?]\w*\d)\w*')
value = "asdfsdf12!"
print(re.match(pattern, value) is not None)

pattern = re.compile('\w+@\w+\.(ru|com|de)')
value = "hello_world123@b.ru"
print(re.match(pattern, value) is not None)

