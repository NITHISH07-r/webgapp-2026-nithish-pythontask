strings="AC30BD40"
letters=""
digits=""
for i in strings:
    if i.isalpha():
        letters = letters+i
    elif i.isdigit():
        digits=digits+i
print(letters)
print(digits)
sumdigits=0
for k in digits:
    sumdigits=int(k)+sumdigits
newchar=letters+str(sumdigits)
print(newchar)





    
     