def count_vowels(text):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    vowels_count=0
    for i in text:
        if i in vowels:
            vowels_count=vowels_count+1
    return vowels_count
text=input("enter a string to count the vowels: ")
count=count_vowels(text)
print("the number of vowels in the given string is ",count)