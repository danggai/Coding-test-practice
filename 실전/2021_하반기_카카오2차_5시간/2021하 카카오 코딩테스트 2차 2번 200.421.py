import json
from urllib import request

headers = {}
base_url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

def api_start(problem: int):
    first_headers = {'X-Auth-Token': 'fdb57647457a900cbe1c1890869337da',"Content-Type": "application/json"}

    data = {
        "problem": problem
    }

    req = request.Request(base_url+"/start", data= data, headers= first_headers)
    res = request.urlopen(req, data=bytes(json.dumps(data), encoding="utf-8"))
 
    data = json.loads(res.read().decode('utf-8'))

    print(data)

    global headers
    headers= {'Authorization': data.get("auth_key"),"Content-Type": "application/json"}


def api_waiting_line():
    global headers

    req = request.Request(base_url+"/waiting_line", headers= headers)
    res = request.urlopen(req)
 
    data = json.loads(res.read().decode('utf-8'))

    return data.get("waiting_line")

def api_game_result():
    global headers

    req = request.Request(base_url+"/game_result", headers= headers)
    res = request.urlopen(req)
 
    data = json.loads(res.read().decode('utf-8'))
    return data.get("game_result")

def api_user_info():
    global headers

    req = request.Request(base_url+"/user_info", headers= headers)
    res = request.urlopen(req)
 
    data = json.loads(res.read().decode('utf-8'))

    return data.get("user_info")

def api_match(pairs: list):
    global headers

    data = {
        "pairs": pairs
    }

    req = request.Request(base_url+"/match", data= data, headers= headers, method="PUT")
    res = request.urlopen(req, data=bytes(json.dumps(data), encoding="utf-8"))
 
    data = json.loads(res.read().decode('utf-8'))

    result = {}
    result["status"] = data.get("status")
    result["time"] = data.get("time")

    print(result)
    return result

def api_change_grade(users: list):
    global headers
    if users == []: return

    commands = []
    for user in users:
        commands.append({
            "id": user["id"],
            "grade": user["grade"]
        })

    data = {
        "commands": commands
    }

    print(data)

    req = request.Request(base_url+"/change_grade", data= data, headers= headers, method="PUT")
    res = request.urlopen(req, data=bytes(json.dumps(data), encoding="utf-8"))
 
    data = json.loads(res.read().decode('utf-8'))

    return data.get("status")

def api_score():
    global headers

    req = request.Request(base_url+"/score", headers= headers)
    res = request.urlopen(req)
 
    data = json.loads(res.read().decode('utf-8'))

    print(data)

def user_matching(waiting_line: list, user_info: list):
    matched_list = []

    for user in waiting_line:
        for info in user_info:
            if (info["id"] == user["id"]):
                user["grade"] = info["grade"]
                break

    sorted(waiting_line, key=lambda x: (x["grade"]))        # grade 정렬

    while len(waiting_line) >= 2:

        matched_team = []
        matched_team.append(waiting_line[0]["id"])
        del waiting_line[0]

        matched_team.append(waiting_line[0]["id"])
        del waiting_line[0]

        matched_list.append(matched_team)

    return matched_list

def calculate_grade(game_result, user_info):

    changed_list = []

    for result in game_result:

        winner = {}
        loser = {}
        winner['id'] = result['win']
        loser['id'] = result['lose']
        
        for user in user_info:
            if user['id'] == winner['id']:
                winner['grade'] = user['grade']
            if user['id'] == loser['id']:
                loser['grade'] = user['grade']

    
        if result['taken'] <= 10 and loser['grade'] > winner['grade'] :
            winner['grade'] -= result['taken']
            loser['grade'] += result['taken']
        else:
            winner['grade'] += result['taken']
            loser['grade'] -= result['taken']

        changed_list.append(winner)
        changed_list.append(loser)

    api_change_grade(changed_list)

def init_grade(user_info: list):
    for user in user_info:
        user["grade"] = 5000

    api_change_grade(user_info)


api_start(2)

result = api_match([])

user_info = api_user_info()
init_grade(user_info)

while (1):
    user_info = api_user_info()

    game_result = api_game_result()

    calculate_grade(game_result, user_info)

    waiting_line = api_waiting_line()

    matched_list = user_matching(waiting_line, user_info)

    result = api_match(matched_list)

    if (result["status"] == "finished"): break

api_score()
    
    
    


