#fabbanoci series for n terms
def fabbonaci(n):
    if n <= 1:
        return n
    else:
        return fabbonaci(n-1) + fabbonaci(n-2)
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fabbonaci series:")
    for i in range(n):
        print(fabbonaci(i),end=" ")

