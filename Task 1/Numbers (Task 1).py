justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("number of members in justce league are : ", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

justice_league[0],justice_league[2]= justice_league[2],justice_league[0]
print(justice_league)


justice_league[5],justice_league[4]=justice_league[4],justice_league[5]
print (justice_league)

justice_league=["Cyborg","Shazam","Hawkgirl","Martian","Manhunter","Green Arrow"]
print(justice_league)

justice_league.sort()
print(justice_league)

new_leader=justice_league[0]
print("new leader is",new_leader)
