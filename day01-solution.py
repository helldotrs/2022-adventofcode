#written by hellmak.com

with open("day01-input", "r") as data:
    txt = data.read()

list_alpha  = txt.split('\n')
list_beta   = []

y = 0
for x in list_alpha:
    if x:
        x = int(x)        
        y += x
    else: 
        list_beta.append(y)
        y = 0
        
list_beta.sort()

print("pt1:")
print(list_beta[-1])
print("pt2:")
print(list_beta[-1]+list_beta[-2]+list_beta[-3])
