import json

data = {"toto":[1,2,3,4],"titi":"fkfkfk"}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print(data["toto"])