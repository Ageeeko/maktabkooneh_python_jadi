gener = {
    'Horror': 0, 'Romance': 0, 'Comedy': 0, 
    'History': 0, 'Adventure': 0, 'Action': 0}
times  = int(input())
for i in range(times):
    detail = input().split(' ')#input().split(' ')
    person , fav_gener = detail[0], detail[1:]
    for i in fav_gener:
        gener[i] = gener[i] +  1
items = gener.items()
items = sorted(items, key=lambda item: (item[1],-(ord(item[0][0])-100)))
items.reverse()
for i in items:
    print("%s : %i"% (i[0],i[1]))
