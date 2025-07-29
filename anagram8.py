def anagram(str1,str2):
    return sorted(str1.replace(" ","").lower()) == sorted(str2.replace(" ","").lower())
str1=input("enter a:")
str2=input("enter b:")
print("anagram", anagram(str1,str2))
