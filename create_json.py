import json

with open("data.json", "w") as file:
    users = {}
    user = {
        "name": "Maciej",
        "email": "maciejtonderski.mt@gmail.com"
    }
    users.append(user)
    json.dump(users, file)