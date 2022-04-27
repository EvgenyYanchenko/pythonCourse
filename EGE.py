d = 81**2017+9**5223-81
counter = 0
while d>0:
    counter+=d%6
    d//=6
    print(d)
print("counter"+str(counter))


