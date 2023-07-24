numbers= []
for i in range(10):
    number = input()
    numbers.append(int(number))
numbers.sort(reverse=True)
number = 0
shomarande = 0
highest = max(numbers)

prime = []
for i in range(2,highest):
    for i2 in range(2,i):
        if i % i2 == 0:
            break
    else:
        prime.append(i)
        
for i in numbers:
    counter = 0
    for i2 in prime:
        if i2 > i:
            break
        if i % i2 == 0 : 
            counter+=1
    if counter > shomarande:
        shomarande = counter
        number = i

print(number,shomarande)
