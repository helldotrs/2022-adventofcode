#written by hellmak.com

with open("day01-input", "r") as data:
    txt = data.read()

list_alpha  = txt.split('\n')
list_beta   = []

print(list_alpha)

print("for loop:")
y = 0
for x in list_alpha:
    if x:
        x = int(x)
        
        y += x
        print(y) #comment out in final version
    else: 
        list_beta.append(y)
        print (list_beta)
        y = 0
        
print("answer:")
print(max(list_beta))
