x = int(input("Enter first numbers"))
y = int(input("Enter second numbers"))
try:
    z = x/y
except Exception as e:
    print(type(e).__name__)
    z = "none"

print("output is ", z)
