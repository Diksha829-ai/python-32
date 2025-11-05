import re
string = """Hello my Number is 123456789 and
my friend's number is 987654321"""
regex = r'\d+'
match = re.findall(regex, string)
print(match)


# find and list all lowercase letters from 'a'to 'e'
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

import re
p = re.compile('ab*')
print(p.findall("ababbaabbb"))
