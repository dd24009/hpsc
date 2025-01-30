print("enter a  number")

x = float(input())
s = 1.0

for k in range(10):
    s = 0.5*(s+x/s)
    

print(s)

