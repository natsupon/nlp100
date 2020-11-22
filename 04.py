import re

word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = word.split()

x = [1,5,6,7,8,9,15,16,19]
ans = {}
for i,w in enumerate(str):
    if i + 1 in x:
        ans[w[:1]] = i + 1
    else:
        ans[w[:2]] = i + 1
print(ans)
