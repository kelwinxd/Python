bugdet=500
place=""
wealth="heath"
result="I go to {}"

if wealth=="heath" and (bugdet>600 and bugdet<1000):
    place="swimming pool"

else:
    place="home"

print(result.format(place))

