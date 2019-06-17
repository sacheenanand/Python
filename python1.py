__author__ = 'sanand'


print("Welcome to california")


sacheen = dict()

words = "Jatheennnnnnnn"

for word in words:
    if word not in sacheen:
        sacheen[word] = 1
    else:
        sacheen[word] += 1
print(sacheen)


d = dict()
letters = "Arinsuvarna"

for u in letters:
    d[u] = d.get(0, 1)+ 1
print(d)


s = dict()
string = "americaindiachinaaustraliacannadasouthafricanewzealand"

for words in string:
    if words not in s:
        s[words] = 1
    else:
        s[words]+=1
print(s)
bigword = None
largest = -1

for k,v in s.items():
    if v > largest:
        bigword = k
        largest = v
        print(k,v)









