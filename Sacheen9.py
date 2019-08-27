__author__ = 'sanand'

__author__ = 'sanand'

# to search for phone numbers
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

Mr Sacheen
Mrs Anand
Ms Arkula
Mr. Arin




1212132311

818-929-4760
650-224-1096
210.222.2345
123*123*1234
800-123-4567
900-321-9876

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

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

