longest = ''
temp = s[0]
for x in range(1,len(s)):
    if s[x] >= temp[-1]:
            temp += s[x]
    else:
            if len(temp) > len(longest):
                longest = temp
            temp = s[x]
if len(temp) > len(longest):
    longest = temp
print("Longets substring in alphabetical order is: " + longest)
