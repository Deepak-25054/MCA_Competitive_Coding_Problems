class upper_lower:
    def convert(self,n):
        a = list(n)
        a[0] = a[0].upper()
        a[-1]=a[-1].upper()
        return ''.join(a)
obj = upper_lower()

n = input("enter the string: ")
print(obj.convert(n))