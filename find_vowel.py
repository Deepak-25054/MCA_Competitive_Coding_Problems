class find_vowel_constant_space:
    def count(self,n):
        vowels = 0
        constant=0
        spaces=0
        for i in n:
            if i.lower() in "aeiou":
                vowels+=1
            elif  i.isalpha():
                constant+=1
            elif i == " ":
                spaces +=1
        print("vowels:", vowels)
        print("costant:", constant)
        print("spaces:", spaces)
obj = find_vowel_constant_space()
n = input("enter a string : ")
obj .count(n)