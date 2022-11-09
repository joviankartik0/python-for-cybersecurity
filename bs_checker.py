import requests
import json

myPlayerId = "28pv9q9p" 

def printCharacter(chosen):
    try:
        for k, v in chosen.items():
            if k == "gears":
                if len(v) == 10:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")" + ", " + v[8]["name"] + "(" + str(v[8]["level"]) + ")" + ", " + v[9]["name"] + "(" + str(v[9]["level"]) + ")").lower()
                elif len(v) == 9:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")" + ", " + v[8]["name"] + "(" + str(v[8]["level"]) + ")").lower()
                elif len(v) == 8:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")").lower()
                elif len(v) == 7:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")").lower()
                elif len(v) == 6:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")").lower()
                elif len(v) == 5:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")").lower()
                elif len(v) == 4:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")").lower()
                elif len(v) == 3:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")").lower()
                elif len(v) == 2:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")").lower()
                elif len(v) == 1:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")").lower()
                else:
                    gears = ""
                print(f"{k}: {gears}") 
            elif k == "starPowers" or k == "gadgets":
                if len(v) == 2:
                    powerOrGadget = (v[0]["name"] + ", " + v[1]["name"]).lower()
                elif len(v) == 1:
                    powerOrGadget = (v[0]["name"]).lower()
                else:
                    powerOrGadget = ""
                print(f"{k}: {powerOrGadget}") 
            else:
                print(f"{k}: {v}")
    except:
        print("-")

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjliZjMyOGQyLTFmNDEtNDQwNC1iNTdjLWY0YWZjOGNkM2ZmZSIsImlhdCI6MTY2NzU1ODM0NCwic3ViIjoiZGV2ZWxvcGVyLzE4NmZlNWQ1LTFhOWQtN2YzMC00YjZlLTA4MTdjN2NhODk0ZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiODcuMjA5LjM3LjM2Il0sInR5cGUiOiJjbGllbnQifV19.7GBb6ndRDM2mWOu1Si7dtZvlaUhnW_PAx2q1VEuO7AxghbvM406TDLNT5D_0iQQ8yCZ7zLpYRQxiNo00z5pN-A"
head = {'Authorization': 'Bearer {}'.format(token)}
base_url = "https://api.brawlstars.com/v1/"

question1 = input("Select what you want to see:\na: Brawlers\nb: Player information\nYour answer: ").lower()
if question1 == "a":
    r = requests.get(f"{base_url}brawlers", headers = head)
    charactersList = r.json()["items"]
    character = input("Type your brawler\nYour answer: ").upper()
    if character == "ALL": 
        try:
            for i in range(len(charactersList)):  
                print("")
                printCharacter(charactersList[i])
        except:
            print("-")
    else: 
        for i in range(len(charactersList)):
            if charactersList[i]["name"] == character:
                print("")
                printCharacter(charactersList[i])
elif question1 == "b":
    playerTag = input("type tag of the player: ")
    player = f"players/%23{playerTag}"
    r = requests.get(f"{base_url}{player}", headers = head)
    playerInfo = r.json()
    characersOrInfo = input("\na: Player Info\nb: All brawlers\nYour answer: ")
    print("")
    if characersOrInfo == "a": 
        for k, v in playerInfo.items():
            if k == "club":
                clubName = v["name"]
                print(f"{k}: {clubName}")
            elif k != "brawlers":
                print(f"{k}: {v}")
    else:
        for i in range(len(playerInfo["brawlers"])):
            printCharacter(playerInfo["brawlers"][i])
            print("")


