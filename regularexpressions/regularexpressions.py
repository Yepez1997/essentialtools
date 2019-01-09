# Regular Expressions 
import re 
import json



whitespace = re.search(r'(?<=-)\w+', 'spam-egg')
abc = re.search(r'(?<=abc)def', 'abcdef')
letters_only = re.match(r'[A-Za-z]*','ASAJD3232KLkkk123')
# searches for 6 consecutive 0's 
a_s = re.search(r'(?:a{6})*', 'aaaaaaaasdaaa,aaa')
# match is like group except easier to index
print(whitespace.group(0))
print(abc.group(0))
print(letters_only.group(0))
print(a_s.group(0))






