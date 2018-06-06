c_bob = 0
for z in range(0,len(s)):
    if(s[z:z+3] == 'bob'):
        c_bob += 1
print("Number of times bob occurs is",c_bob)
