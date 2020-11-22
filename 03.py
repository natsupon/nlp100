import re
word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word = re.sub('[,.]','',word)
str = word.split()

ans = [len(i) for i in str]
print(ans)