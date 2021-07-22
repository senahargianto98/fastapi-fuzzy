from fuzzywuzzy import process,fuzz
import re
# for process library,
# query = "geeks for geeks"
# choices = ["geeks for geek"]
# a = format(process.extractOne("sena", ["sena","febrisena"]))

a = "geeks for geeks"
b = ["geeks for geek"]

for i in zip(a,b):
    c = "{}".format(process.extractOne(a,b),i)
    d = re.sub('\d', '', c)
    e = re.sub(',',"",d)
    f = e.replace(' ','')
    h = f.replace('(', '').replace(')', '')


# print (process.extract(query, choices))
print (h)
# print (process.extractOne(query, choices)) 
# for i,j in zip()