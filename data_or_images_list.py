import re
with open('soup.txt', 'r') as f:
    data = f.read()
list = data.replace('[', ' ').replace(']', ' ').replace('\"', ' ').replace('(', ' ').replace(')', ' ').split()

links = []
for i in list:
    if re.search('http', i) and i[-4] == '.' and i[-3] in 'jspg':
        links.append(i)
    elif re.search('data:image', i):
        links.append(i)
    else:
        continue
