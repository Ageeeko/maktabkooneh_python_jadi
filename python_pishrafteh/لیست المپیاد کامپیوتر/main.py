number = int(input())
female_list = []
male_list = []

for i in range(number):
    winner = input().split(".")
    winner[1] = winner[1].lower().capitalize()
    if winner[0] == "f":
        female_list.append(winner)
    elif winner[0] == "m":
        male_list.append(winner)
female_list = sorted(female_list,key=lambda item : (item[1]))
male_list = sorted(male_list,key=lambda item : (item[1]))
list1 = [female_list,male_list]
for gender in list1:
    for i in gender:
        print(" ".join(i))
