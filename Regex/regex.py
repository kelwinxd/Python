import re

string = "kelwin"
pattern = "k*elwin"

if re.search(pattern, string):
    print("Match")
else:
    print("None bitch")
