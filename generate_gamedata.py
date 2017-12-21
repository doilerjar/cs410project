'''
CS410 Project
Kevin Kang

generate_gamedata.py uses igdb.com's REST api to collect a random list of games, and store them
in games.dat file in metapy format
'''
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2
import random as rand
import json
import ast

# Generate a random list of game id's
rand_set = []

for i in range(1000):
    found = False
    while not found:
        rand_number = rand.randint(1, 50000)
        if len(rand_set) == 0:
            rand_set.append(rand_number)
            found = True
        else:
            if rand_number not in rand_set:
                rand_set.append(rand_number)
                found = True

# url = 'https://api-2445582011268.apicast.io/games/2?fields=*'
filename = "games/games.dat"
for game_id in rand_set:
    url = 'https://api-2445582011268.apicast.io/games/' + str(game_id) + '?fields=*'

    req = Request(url)
    req.add_header('user-key', '5bd58b929b267943fc7b35f95010c181')
    req.add_header('Accept', 'application/json')
    response = urlopen(req).read()
    print(response)
    # filename = "games/" + str(game_id) + '.txt'
    game_data = response.decode("utf-8")
    try:
        game_data = ast.literal_eval(game_data)[0]
    except:
        continue
    else:
        try:
            summary = game_data['summary']
            summary = summary.replace('\n','').replace('\r','')
            output = str(game_data['id']) + ' ' + game_data['name'] + ' ' + summary + ' .' + '\n'
        except:
            print("Error")
        else:
            print(output)
            with open(filename,'a') as file:
                file.write(output)