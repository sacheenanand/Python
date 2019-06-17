__author__ = 'sanand'

import re

text_to_search = '''
Sacheen Anand
1441 creek side dr
apt 2067
walnut creek ca 94596

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
.[{}]?/''\

cat
mat
rat
bat



1212132311

818-929-4760
650-224-1096
210.222.2345
123*123*1234

sacheen.com

Ha HaHaHa



my name is Sacheen working in san francisco

I want to learn Python and be a pro in it

my dream jobs working is in
google
facebook
tesla
twitter
arin_suvarna

'''

sentence = 'Sacheen anand carlos bee blvd hayward ca 94542 end'

print(r'\tTab')

pattern = re.compile(r'end$')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print(text_to_search[66:69])
print(text_to_search[120:121])


