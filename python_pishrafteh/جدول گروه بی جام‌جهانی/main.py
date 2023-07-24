team1 = ["Iran","Iran","Iran","Spain","Spain","Portugal"]
team2 = ["Spain","Portugal","Morocco","Portugal","Morocco","Morocco"]
result_dict = dict()
for t1,t2 in zip(team1,team2):
    t1goal,t2goal = input().split("-")
    t1goal = int(t1goal)
    t2goal = int(t2goal)

    if t1 not in result_dict:
        result_dict[t1] = {"wins":0 , "loses":0 , 'draws':0 , "goal zadeh":0 ,"goal khorde":0, "points":0}
    if t2 not in result_dict:
        result_dict[t2] = {"wins":0 , "loses":0 , 'draws':0 , "goal zadeh":0 ,"goal khorde":0, "points":0}

    if t1goal > t2goal:
        result_dict[t1]["wins"] = result_dict[t1]["wins"] + 1
        result_dict[t1]["points"] = result_dict[t1]["points"] + 3
        result_dict[t1]["goal zadeh"] =  result_dict[t1]["goal zadeh"] + t1goal 
        result_dict[t1]["goal khorde"] =  result_dict[t1]["goal khorde"] + t2goal 

        result_dict[t2]["loses"] =result_dict[t2]["loses"] +1
        result_dict[t2]["goal zadeh"] =  result_dict[t2]["goal zadeh"] + t2goal 
        result_dict[t2]["goal khorde"] =  result_dict[t2]["goal khorde"] + t1goal 

    elif t2goal > t1goal:
        result_dict[t2]["wins"] = result_dict[t2]["wins"] + 1
        result_dict[t2]["points"] = result_dict[t2]["points"] + 3
        result_dict[t1]["goal zadeh"] =  result_dict[t1]["goal zadeh"] + t1goal 
        result_dict[t1]["goal khorde"] =  result_dict[t1]["goal khorde"] + t2goal 

        result_dict[t1]["loses"] =result_dict[t1]["loses"] +1
        result_dict[t2]["goal zadeh"] =  result_dict[t2]["goal zadeh"] + t2goal 
        result_dict[t2]["goal khorde"] =  result_dict[t2]["goal khorde"] + t1goal 


    elif t2goal == t1goal:
        result_dict[t1]["draws"] = result_dict[t1]["draws"] + 1
        result_dict[t2]["draws"] = result_dict[t2]["draws"] + 1

        result_dict[t2]["goal zadeh"] =  result_dict[t2]["goal zadeh"] + t2goal 
        result_dict[t2]["goal khorde"] =  result_dict[t2]["goal khorde"] + t1goal 
        result_dict[t1]["goal zadeh"] =  result_dict[t1]["goal zadeh"] + t1goal 
        result_dict[t1]["goal khorde"] =  result_dict[t1]["goal khorde"] + t2goal 
        result_dict[t2]["points"] = result_dict[t2]["points"] + 1
        result_dict[t1]["points"] = result_dict[t1]["points"] + 1



items = result_dict.items()
items = sorted(items,key=lambda item:(-(item[1]["points"]-100),-(item[1]["wins"]-100),item[0][0]))
for i in items:
    print(f"{i[0]}  wins:{i[1]['wins']} , loses:{i[1]['loses']} , draws:{i[1]['draws']} , goal difference:{i[1]['goal zadeh'] -i[1]['goal khorde']} , points:{i[1]['points']}")

