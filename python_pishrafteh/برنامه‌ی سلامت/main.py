class school:
    def __init__(self,number_of_students):
        self.quantity = number_of_students

    def get_age(self,ages:list):
        for index,i in enumerate(ages):
            ages[index] = int(ages[index])
        return sum(ages)/self.quantity
    
    def get_height(self,heights:list):
        for index,i in enumerate(heights):
            heights[index] = int(heights[index])        
        return sum(heights)/self.quantity
    
    def get_weights(self,weights):
        for index,i in enumerate(weights):
            weights[index] = int(weights[index])        
        return sum(weights)/self.quantity
    
dict1 = dict()
for i in ["A","B"]:
    students = school(float(input()))
    dict1[i] = {
        "age": students.get_age(input().split()),
        "height":students.get_height(input().split()),
        "weight":students.get_weights(input().split())
        }
tmp = []
for i in dict1:
    print(dict1[i]["age"])
    print(dict1[i]["height"])
    print(dict1[i]["weight"])

    tmp.append((i,dict1[i]["weight"]))
if tmp[1][1] == tmp[0][1]:
    print("Same")
else:
    max_tmp = max(tmp[1][1],tmp[0][1])
    if max_tmp in tmp[1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
